#!/usr/bin/env python3
"""
AutoXMate — Help Text Flag Parser & Enricher
Parses help_texts/*.txt, extracts all flags, merges into parsed_params/*.json,
and updates tool YAML frontmatter with complete parameters.

Usage:
  python3 scripts/extract-tool-flags.py                    # Process all tools (default: dry-run)
  python3 scripts/extract-tool-flags.py --apply            # Actually write changes
  python3 scripts/extract-tool-flags.py --tool nmap        # Single tool
  python3 scripts/extract-tool-flags.py --stats            # Summary only
"""

import os, sys, json, re, yaml
from pathlib import Path
from collections import OrderedDict

HELP_DIR = Path(__file__).parent.parent / "data" / "help_texts"
PARAMS_DIR = Path(__file__).parent.parent / "data" / "parsed_params"
TOOLS_DIR = Path(__file__).parent.parent / "src" / "content" / "tools"

# ---------------------------------------------------------------------------
# Help text → flag extraction
# ---------------------------------------------------------------------------

# Patterns for flag lines in help text
FLAG_LINE_RE = re.compile(
    r'^\s{2,}'                          # indented (helps skip headers/examples)
    r'('
    r'(?:--?[a-zA-Z0-9][a-zA-Z0-9?_*-]*)'  # flag itself
    r'(?:\s*[/,;]\s*'                      # combined like -n/-R, -f; --mtu
    r'(?:--?[a-zA-Z0-9][a-zA-Z0-9?_*-]*))?'
    r')'
    r'(?:[<\[]'                          # optional <arg> or [arg]
    r'[^>\]\n]*'
    r'[>\]])?'
    r'(?:\s*[/,;]\s*'                    # also combined like -oN/-oX/-oS/-oG
    r'(?:--?[a-zA-Z0-9][a-zA-Z0-9?_*-]*)'
    r'(?:[<\[]'
    r'[^>\]\n]*'
    r'[>\]])?)*'
    r'(?:\s*=|=\s*[<\[])?'               # optional =<value> or =<arg>
    r'(?:\s*[:=]|$)'                     # separator : or = or end
)

def parse_help_text(text, tool_name):
    """
    Parse help text and extract unique flags with their descriptions.
    Returns dict of flag_name → {aliases, description, has_arg}
    """
    flags = OrderedDict()
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        # Skip header lines (all caps, no indent), example lines, usage lines
        if (stripped.isupper() and len(stripped) > 2 and ' ' not in stripped.strip()):
            continue
        if stripped.startswith('Usage:') or stripped.startswith('Ex:') or stripped.startswith('Example'):
            continue
        if not line or line[0] == '\n':  # skip empty lines
            continue
        if not line[0].isspace():  # must be indented (space or tab)
            continue
        if stripped.startswith('---'):
            continue
            
        # Extract flags from the line
        line_flags = extract_line_flags(stripped, tool_name)
        if not line_flags:
            continue
        
        # Only accept lines that look like real flag definitions (not prose artifacts)
        if not is_real_flag_line(stripped, line_flags):
            continue

        # Extract description (everything after the last flag-like content)
        desc = extract_description(stripped, line_flags)
        
        # Merge with dedup
        primary_flag = line_flags[0]
        if primary_flag not in flags:
            flags[primary_flag] = {
                'aliases': line_flags,
                'description': desc,
                'has_arg': has_argument_flag(stripped, primary_flag),
            }
        elif desc and not flags[primary_flag]['description']:
            flags[primary_flag]['description'] = desc
            # Merge any new aliases
            for f in line_flags:
                if f not in flags[primary_flag]['aliases']:
                    flags[primary_flag]['aliases'].append(f)
    
    return flags


# Words that are NOT flags even if they start with '-'
NON_FLAG_WORDS = {
    '-a', '-an', '-the', '-or', '-and', '-in', '-on', '-at', '-to', '-for',
    '-of', '-by', '-with', '-from', '-not', '-but', '-can', '-all', '-any',
    '-each', '-every', '-some', '-no', '-more', '-most', '-less', '-that',
    '-this', '-these', '-those', '-is', '-are', '-was', '-were', '-be', '-been',
    '-being', '-have', '-has', '-had', '-do', '-does', '-did', '-will', '-would',
    '-shall', '-should', '-may', '-might', '-must', '-could', '-need', '-dare',
    '-files', '-categories', '-separated', '-hosts', '-ports', '-services',
    '-target', '-targets', '-protocol', '-protocols', '-options', '-option',
    '-name', '-names', '-value', '-values', '-type', '-types', '-list',
    '-file', '-dir', '-directory', '-path', '-paths', '-key', '-keys',
    '-number', '-numbers', '-string', '-strings', '-line', '-lines',
    '-output', '-inputs', '-input', '-result', '-results', '-log', '-logs',
    '-time', '-times', '-date', '-dates', '-config', '-configs',
    '-only', '-also', '-like', '-just', '-while', '-when', '-where',
    '-how', '-what', '-which', '-who', '-why', '-set', '-gets', '-gets',
    '-example', '-examples', '-ex', '-see', '-note', '-tip', '-info',
    '-default', '-defaults', '-standard', '-common', '-basic', '-simple',
    '-advanced', '-expert', '-custom', '-user', '-users', '-group', '-groups',
}

# Lines that are NOT flag definitions even if they look like them
NON_FLAG_LINE_PREFIXES = (
    'ex:', 'example:', 'note:', 'tip:', 'see:', 'usage:', 'info:',
    'also', 'and', 'or', 'the', 'for', 'can', 'will', 'may',
    'default:', 'e.g.', 'i.e.',
)

def extract_line_flags(stripped, tool_name):
    """Extract one or more flag names from a help line."""
    flags = []
    line = stripped
    
    # Skip lines that obviously aren't flag definitions
    if not line:
        return flags
    first_word = line.split()[0] if line.split() else ''
    if not first_word.startswith('-'):
        return flags  # line must start with a flag
    if first_word.lower() in NON_FLAG_LINE_PREFIXES or first_word.lower().rstrip(':.,;') in NON_FLAG_LINE_PREFIXES:
        return flags
    
    # Remove the description part (after : or -- or multiple spaces)
    desc_cut = len(line)
    colon_depth = 0
    for j, ch in enumerate(line):
        if ch == '<' or ch == '[':
            colon_depth += 1
        elif ch == '>' or ch == ']':
            colon_depth -= 1
        elif ch == ':' and colon_depth <= 0:
            desc_cut = j
            break
    
    flag_part = line[:desc_cut].strip()
    
    # Extract individual flags
    flag_pattern = r'(--?[a-zA-Z0-9][a-zA-Z0-9?_*-]*)'
    
    for match in re.finditer(flag_pattern, flag_part):
        flag = match.group(1)
        # Filter false positives
        if flag.startswith('---'):
            continue
        if len(flag) < 2:
            continue
        if flag.lower() in NON_FLAG_WORDS:
            continue
        # Skip if looks like a value rather than a flag (e.g., part of <arg>)
        flags.append(flag)
    
    return flags


# ---------------------------------------------------------------------------
# Flag line validation — filter out man-page prose artifacts
# ---------------------------------------------------------------------------

# Words commonly used in prose that are NOT flags
PROSE_WORDS = set()
for w in [
    'access', 'active', 'action', 'address', 'after', 'again', 'alias',
    'allow', 'alphabetical', 'already', 'also', 'always', 'anything',
    'appear', 'append', 'apply', 'argument', 'assume', 'attach',
    'attempt', 'author', 'available', 'backward', 'background', 'base',
    'basic', 'become', 'before', 'begin', 'beginning',
    'below', 'blank', 'block', 'body', 'both', 'bottom',
    'break', 'bring', 'buffer', 'build', 'built', 'call', 'cancel',
    'capability', 'capture', 'case', 'center', 'certain', 'change',
    'character', 'check', 'child', 'choose', 'clear', 'client',
    'close', 'code', 'color', 'column', 'combine', 'command',
    'common', 'compare', 'complete', 'connect', 'console', 'content',
    'context', 'continue', 'control', 'convert', 'copy', 'correct',
    'count', 'create', 'current', 'cursor', 'custom', 'cycle',
    'daemon', 'data', 'deactivate', 'debug', 'default', 'define',
    'delay', 'delete', 'depend', 'depth', 'describe', 'design',
    'destroy', 'detach', 'detail', 'determine', 'device', 'disable',
    'discard', 'disconnect', 'display', 'distance', 'document',
    'done', 'double', 'down', 'draw', 'drop', 'during', 'each',
    'echo', 'edge', 'edit', 'effect', 'either', 'element', 'empty',
    'enable', 'end', 'enforce', 'enter', 'entire', 'entry', 'equal',
    'error', 'escape', 'event', 'every', 'exact', 'exclude', 'execute',
    'exist', 'exit', 'expand', 'expect', 'expire', 'export', 'extend',
    'extra', 'extract', 'failed', 'field', 'fill', 'filter',
    'final', 'find', 'finish', 'first', 'fix', 'flag', 'flush', 'focus',
    'follow', 'font', 'force', 'foreground', 'format', 'forward',
    'free', 'fresh', 'front', 'full', 'function', 'future', 'generate',
    'get', 'give', 'global', 'grant', 'graph', 'handle',
    'hang', 'have', 'head', 'header', 'height', 'hidden',
    'hide', 'hierarchy', 'high', 'history', 'hold', 'home', 'hook',
    'horizontal', 'icon', 'identify', 'idle', 'ignore',
    'immediate', 'include', 'increment', 'index', 'indicate', 'indirect',
    'individual', 'info', 'inherit', 'init', 'initial', 'inject',
    'inline', 'input', 'insert', 'inside', 'install', 'instance',
    'interact', 'internal', 'interval', 'inverse', 'invert', 'issue',
    'item', 'join', 'jump', 'just', 'justify', 'keep', 'kill',
    'label', 'language', 'large', 'last', 'late', 'launch', 'layer',
    'layout', 'leading', 'leave', 'left', 'length', 'less', 'level',
    'life', 'lift', 'light', 'limit', 'load',
    'locate', 'lock', 'login', 'look', 'loop',
    'machine', 'mail', 'main', 'major', 'make', 'manage', 'manual',
    'map', 'mark', 'match', 'maximum', 'measure', 'medium', 'member',
    'memory', 'menu', 'merge', 'message', 'metadata', 'method', 'middle',
    'minimum', 'minor', 'minute', 'mirror', 'mode', 'model', 'modify',
    'module', 'monitor', 'mouse', 'move', 'multi', 'multiple',
    'narrow', 'native', 'navigate', 'near', 'need', 'network', 'new',
    'next', 'node', 'normal', 'nothing', 'notice',
    'obsolete', 'offset', 'old', 'oneshot', 'only', 'open',
    'operation', 'order', 'origin', 'other', 'otherwise',
    'outside', 'overlap', 'override', 'overview',
    'owner', 'package', 'pad', 'page', 'pane', 'panel', 'parameter',
    'parent', 'parse', 'part', 'partial', 'partition', 'pass',
    'pattern', 'pause', 'perform', 'period', 'permit', 'persist',
    'pipe', 'place', 'point', 'policy', 'poll', 'pool', 'portion',
    'position', 'positive', 'possible', 'post', 'power', 'prefix',
    'prepend', 'preserve', 'press', 'prevent', 'previous', 'process',
    'produce', 'program', 'progress', 'prompt', 'protect', 'provide',
    'purge', 'push', 'put', 'query', 'queue', 'quit',
    'raise', 'range', 'rank', 'rate', 'reach', 'read', 'ready',
    'real', 'rebuild', 'receive', 'recent', 'record', 'recover',
    'redirect', 'reduce', 'refer', 'refresh', 'region', 'register',
    'reload', 'remain', 'remember', 'remote', 'remove', 'rename',
    'render', 'repeat', 'replace', 'reply', 'report', 'request',
    'require', 'reset', 'resize', 'resolve', 'resource', 'respond',
    'restart', 'restore', 'restrict', 'result', 'resume', 'retain',
    'return', 'reuse', 'reverse', 'review', 'revoke', 'right', 'ring',
    'role', 'root', 'rotate', 'round', 'route', 'row', 'rule', 'run',
    'save', 'scale', 'scan', 'schedule', 'scheme', 'scope', 'screen',
    'script', 'scroll', 'search', 'second', 'section', 'secure',
    'select', 'send', 'sensitive', 'separate', 'sequence', 'serial',
    'server', 'service', 'session', 'setting', 'setup', 'share',
    'shell', 'shift', 'short', 'show', 'shuffle', 'shutdown', 'side',
    'signal', 'silent', 'similar', 'simple', 'single', 'size', 'skip',
    'slave', 'sleep', 'slide', 'small', 'snapshot', 'socket', 'sort',
    'source', 'space', 'span', 'spawn', 'special', 'specific', 'specify',
    'speed', 'split', 'stack', 'stage', 'stamp', 'standard', 'standby',
    'start', 'state', 'static', 'statistics', 'status',
    'step', 'stop', 'store', 'stream', 'strict',
    'strip', 'structure', 'style', 'subject', 'submit', 'subnet',
    'subscribe', 'subsequent', 'subset', 'substitute', 'substring',
    'suffix', 'summary', 'super', 'support', 'suppress', 'suspend',
    'switch', 'symbol', 'sync',
    'tab', 'table', 'tag', 'task', 'template',
    'terminal', 'terminate', 'test', 'text', 'theme', 'thread', 'threshold',
    'through', 'throw', 'tick', 'ticket',
    'timeout', 'timer', 'timestamp', 'tls', 'toggle', 'token',
    'top', 'total', 'touch', 'track', 'traffic', 'trailer',
    'transaction', 'transfer', 'transform', 'transient', 'transition',
    'translate', 'transparent', 'transport', 'trap', 'trash',
    'traverse', 'tree', 'trigger', 'trim',
    'true', 'truncate', 'trust', 'try', 'turn',
    'unalias', 'unavailable', 'unbind', 'unchecked', 'unconditional',
    'uncompress', 'under', 'undo', 'unescape', 'unexpand', 'unfold',
    'unhook', 'unidirectional', 'uninstall', 'union', 'unique', 'unit',
    'unix', 'unknown', 'unlimited', 'unlink', 'unload', 'unlock',
    'unmark', 'unmount', 'unregister', 'unset', 'unsorted', 'untar',
    'unused', 'unwatch', 'update', 'upgrade', 'upload', 'upper',
    'uptime', 'usage', 'using', 'usual', 'utf', 'uuid', 'valid',
    'validate', 'variable', 'vector', 'vendor',
    'verify', 'vertical', 'view', 'visible', 'visit',
    'volume', 'wait', 'wake', 'wall', 'want', 'warn', 'watch',
    'wave', 'weak', 'web', 'weight', 'wide', 'width', 'wild',
    'word', 'working', 'wrap', 'xfer', 'yank', 'zone',
]:
    PROSE_WORDS.add('-' + w)
    PROSE_WORDS.add('--' + w)


def is_real_flag_line(line, line_flags):
    """
    Determine if a line contains actual flag definitions vs prose artifacts.
    
    A real flag definition has ONE of these traits:
    1. Long flag (--xxx) present
    2. Flags followed by <arg> or [...] (takes argument)
    3. Multiple flags present (separated by / or ,)
    4. Flag followed by colon(:) or double-space → description
    5. Short flag (single - plus 1-3 chars)
    """
    first_flag = line_flags[0]
    
    # Reject prose words that aren't real flags
    if first_flag.lower() in PROSE_WORDS:
        return False
    
    # Reject if the first flag looks like a word (single dash, >3 chars after dash)
    # unless it would also match the other acceptance criteria below
    is_short = first_flag.startswith('-') and not first_flag.startswith('--')
    if is_short:
        flag_body = first_flag[1:]
        if len(flag_body) > 4:
            return False
    
    # Trait 1: Has a long flag
    if any(f.startswith('--') for f in line_flags):
        return True
    
    # Trait 2: Has <arg> or [...] right after a flag
    for f in line_flags:
        idx = line.find(f)
        if idx >= 0:
            after = line[idx + len(f):].strip()
            if after.startswith('<') or after.startswith('['):
                return True
    
    # Trait 3: Multiple flags separated by / or ,
    if len(line_flags) > 1:
        return True
    
    # Trait 4: Flag followed by colon, or description pattern
    first_flag_idx = line.find(first_flag)
    if first_flag_idx >= 0:
        after_flag = line[first_flag_idx + len(first_flag):].strip()
        if after_flag.startswith(':'):
            return True
        # Check for description text
        desc_text = re.sub(r'^[<\[][^>\]>]*[>\]]\s*', '', after_flag)
        desc_text = re.sub(r'^[/,]\s*', '', desc_text)
        desc_text = re.sub(r'^:\s*', '', desc_text)
        if desc_text and (desc_text[0].isupper() or len(desc_text) > 20):
            return True
    
    # Trait 5: Short flag — 1-3 chars after single dash (like -sV, -p, -oN)
    if is_short:
        flag_body = first_flag[1:]
        if 1 <= len(flag_body) <= 3 and flag_body.isalnum():
            return True
    
    return False

def has_argument_flag(line, primary_flag):
    """Check if a flag takes an argument."""
    # Check if there's <...> or [...] right after the flag
    # Or =<something> or =[something]
    after_flag = line[line.index(primary_flag) + len(primary_flag):].strip() if primary_flag in line else ""
    if after_flag.startswith('<') or after_flag.startswith('['):
        return True
    if after_flag.startswith('=') and (after_flag[1:].startswith('<') or after_flag[1:].startswith('[')):
        return True
    return False


def extract_description(line, line_flags):
    """Extract description text after flag(s) and separators."""
    # Find where flags end
    flag_part_end = 0
    for flag in line_flags:
        idx = line.index(flag, flag_part_end) if flag in line[flag_part_end:] else -1
        if idx >= 0:
            flag_part_end = idx + len(flag)
            # Skip past any <arg>
            rest = line[flag_part_end:].strip()
            if rest.startswith('<') or rest.startswith('['):
                # Find the closing bracket
                depth = 0
                for j, ch in enumerate(rest):
                    if ch == '<' or ch == '[':
                        depth += 1
                    elif ch == '>' or ch == ']':
                        depth -= 1
                        if depth <= 0:
                            flag_part_end = len(line) - len(rest) + j + 1
                            break
        
        # Check for = after flag
        rest = line[flag_part_end:].strip()
        if rest.startswith('='):
            # Find end of =value
            eq_content = rest[1:]
            space_idx = eq_content.find(' ')
            if space_idx >= 0:
                flag_part_end += 1 + space_idx
            else:
                flag_part_end += len(rest)  # =value is the last thing on line
                rest = ''
    
    rest = line[flag_part_end:].strip()
    # Remove leading colon, comma, dash separator
    rest = re.sub(r'^[:,\-]\s*', '', rest).strip()
    
    # Remove trailing options like [default: ...]
    rest = re.sub(r'\s*\[default:[^\]]*\]', '', rest).strip()
    rest = re.sub(r'\s*\(.*\)$', '', rest).strip() if len(rest.split('(')[0]) < 10 else rest
    
    return rest


def canonical_flag_name(flag):
    """Get canonical short form of a flag for dedup."""
    name = flag.lstrip('-')
    name = re.sub(r'[<\[]', '', name)
    name = name.strip()
    return name


# ---------------------------------------------------------------------------
# Params merging
# ---------------------------------------------------------------------------

def build_param_entry(flag, info, existing_params):
    """Build a parameter entry from a flag, reusing existing data when possible."""
    canonical = canonical_flag_name(flag)
    name = canonical.replace('-', '-')
    
    # Check if this flag already exists in params (by alias)
    for ep in existing_params:
        for alias in ep.get('aliases', []):
            alias_flag = alias.split()[0] if alias else ''
            if alias_flag == flag:
                # Update description if we have a better one
                if info['description'] and not ep.get('description'):
                    ep['description'] = info['description']
                return ep
    
    # Check by flag name matching (short vs long)
    short_flag = None
    long_flag = None
    for ep in existing_params:
        for alias in ep.get('aliases', []):
            alias_flag = alias.split()[0] if alias else ''
            if alias_flag.startswith('--') and len(alias_flag) > 3:
                long_flag = ep
            elif alias_flag.startswith('-') and not alias_flag.startswith('--') and len(alias_flag) == 2:
                short_flag = ep
    
    # New entry
    entry = {
        'name': name,
        'template_key': name,
        'type': 'string' if info['has_arg'] else 'boolean',
        'required': False,
        'default_value': None,
        'description': info.get('description', ''),
        'aliases': sorted(info['aliases'], key=len),
    }
    return entry


# ---------------------------------------------------------------------------
# YAML tool file update
# ---------------------------------------------------------------------------

FRONTMATTER_END_RE = re.compile(r'^---\s*$', re.MULTILINE)


def update_tool_yaml(tool_name, params):
    """Update the parameters section in a tool's YAML frontmatter."""
    tool_file = TOOLS_DIR / f"{tool_name}.md"
    if not tool_file.exists():
        return False
    
    content = tool_file.read_text()
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    try:
        data = yaml.safe_load(parts[1])
    except:
        return False
    
    if not data:
        return False
    
    old_count = len(data.get('parameters', []))
    
    # Build updated parameters
    # Convert params dict to list ordered by: existing params preserved, new ones appended
    existing_params = data.get('parameters', [])
    
    # Track which existing params we keep
    updated_params = list(existing_params)  # preserve existing order
    
    # Add any missing params
    existing_flags = set()
    for ep in existing_params:
        for alias in ep.get('aliases', []):
            flag = alias.split()[0] if alias else ''
            if flag.startswith('-'):
                existing_flags.add(flag)
        # Also check by name
        if ep.get('name'):
            existing_flags.add('--' + ep['name'])
            existing_flags.add('-' + ep['name'][0] if ep['name'] else '')
    
    new_count = 0
    for flag, info in params.items():
        if flag not in existing_flags:
            # Double-check: is this truly new?
            is_new = True
            for ef in existing_flags:
                if canonical_flag_name(ef) == canonical_flag_name(flag):
                    is_new = False
                    break
            if is_new:
                entry = build_param_entry(flag, info, existing_params)
                updated_params.append(entry)
                new_count += 1
                existing_flags.add(flag)
    
    if new_count == 0:
        return False
    
    data['parameters'] = updated_params
    
    # Write back
    new_yaml = yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)
    new_content = f"---\n{new_yaml}---\n" + parts[2]
    tool_file.write_text(new_content)
    return old_count, new_count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = '--apply' not in sys.argv
    single_tool = None
    if '--tool' in sys.argv:
        idx = sys.argv.index('--tool')
        if idx + 1 < len(sys.argv):
            single_tool = sys.argv[idx + 1]
    
    only_stats = '--stats' in sys.argv
    
    help_files = sorted(HELP_DIR.glob('*.txt'))
    if single_tool:
        help_files = [HELP_DIR / f"{single_tool}.txt"]
        if not help_files[0].exists():
            print(f"Error: help_text/{single_tool}.txt not found")
            sys.exit(1)
    
    total_missing = 0
    total_updated = 0
    total_tools_with_gaps = 0
    
    for hf in help_files:
        tool_name = hf.stem
        
        # Read existing params
        params_file = PARAMS_DIR / f"{tool_name}.json"
        existing_params = []
        if params_file.exists():
            existing_params = json.loads(params_file.read_text())
        
        # Parse help text
        text = hf.read_text(encoding='utf-8', errors='replace')
        parsed_flags = parse_help_text(text, tool_name)
        
        if not parsed_flags:
            continue
        
        # Find gaps
        parsed_flag_set = set(parsed_flags.keys())
        
        existing_flag_set = set()
        for ep in existing_params:
            for alias in ep.get('aliases', []):
                flag = alias.split()[0] if alias else ''
                if flag.startswith('-'):
                    existing_flag_set.add(flag)
            if ep.get('name'):
                existing_flag_set.add('--' + ep['name'].replace('_', '-').replace('flag-', '-'))
        
        # Normalize comparison
        def normalize_flag(f):
            f = f.lower()
            return re.sub(r'[_\-\s]', '', f)
        
        existing_norm = {normalize_flag(f): f for f in existing_flag_set}
        missing = []
        for pf in parsed_flag_set:
            if normalize_flag(pf) not in existing_norm:
                missing.append(pf)
        
        if not missing:
            continue
            
        total_tools_with_gaps += 1
        total_missing += len(missing)
        
        if only_stats:
            if len(missing) <= 3:
                continue
            print(f"  {tool_name}: {len(missing)} missing — {', '.join(missing[:6])}{'...' if len(missing) > 6 else ''}")
            continue
        
        if dry_run:
            if len(missing) > 3:
                print(f"  {tool_name}: {len(missing)} new flags (parsed {len(parsed_flags)} total, have {len(existing_flag_set)})")
                print(f"    e.g. {', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}")
            continue
        
        # Build merged params
        updated_params = list(existing_params)
        seen_flags = set(existing_flag_set)
        
        for flag in missing:
            info = parsed_flags[flag]
            # Check if alias already covered
            already_covered = False
            for alias in info.get('aliases', []):
                if normalize_flag(alias) in existing_norm:
                    already_covered = True
                    break
            
            if not already_covered:
                entry = build_param_entry(flag, info, existing_params)
                updated_params.append(entry)
                seen_flags.add(flag)
        
        # Write updated params
        params_file.write_text(json.dumps(updated_params, indent=2))
        total_updated += len(updated_params) - len(existing_params)
        
        # Also update the tool YAML
        update_tool_yaml(tool_name, parsed_flags)
    
    print(f"\n=== Summary ===")
    print(f"Help texts processed: {len(help_files)}")
    print(f"Tools with gaps: {total_tools_with_gaps}")
    print(f"Total missing flags: {total_missing}")
    if not dry_run:
        print(f"Total params updated: {total_updated}")
    else:
        print(f"(dry-run — pass --apply to write changes)")


if __name__ == '__main__':
    main()
