#!/usr/bin/env python3
"""
AutoXMate — Update tool YAML frontmatter with enriched parameters from parsed_params/*.json
Appends new parameter entries to the `parameters:` section of each tool's markdown file,
preserving all existing content and formatting.
"""
import json, os, re, sys
from pathlib import Path

TOOLS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools")
PARAMS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/data/parsed_params")

def param_to_yaml(param, indent=2):
    """Generate YAML for a single parameter entry, matching the site's format."""
    prefix = " " * indent + "- "
    
    lines = []
    # name
    lines.append(f"{prefix}name: {param['name']}")
    # type
    type_str = param.get('type', 'boolean')
    if param.get('has_arg'):
        type_str = 'arg'
    lines.append(f"{' ' * (indent+2)}type: {type_str}")
    # required
    lines.append(f"{' ' * (indent+2)}required: {'true' if param.get('required') else 'false'}")
    # default (if has arg type, add a placeholder)
    if type_str != 'boolean':
        default = param.get('default_value', '')
        lines.append(f"{' ' * (indent+2)}default: {default if default else 'null'}")
    # description
    desc = param.get('description', '').replace('"', '\\"')
    lines.append(f"{' ' * (indent+2)}description: \"{desc}\"")
    # aliases
    aliases = param.get('aliases', [])
    # Filter aliases to unique, non-empty
    aliases = [a for a in aliases if a.strip() and a.startswith('-')]
    if aliases:
        lines.append(f"{' ' * (indent+2)}aliases:")
        for alias in aliases:
            lines.append(f"{' ' * (indent+4)}- \"{alias}\"")
    return "\n".join(lines)

def load_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file. Returns (frontmatter_text, body_text, lines)."""
    text = filepath.read_text()
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, text, lines
    
    # Find closing ---
    end = 1
    while end < len(lines):
        if lines[end].strip() == '---':
            break
        end += 1
    else:
        return None, text, lines
    
    frontmatter = '\n'.join(lines[1:end])
    body = '\n'.join(lines[end+1:])
    return frontmatter, body, lines[:end+1]

def param_name_from_yaml(line):
    """Extract param name from a YAML line like '  - name: verbose'"""
    m = re.match(r'^\s*-\s*name:\s*(.+)', line)
    return m.group(1).strip() if m else None

def update_tool_file(tool_name):
    """Update a single tool markdown file with missing parameters."""
    # Find the tool file
    candidates = [
        TOOLS_DIR / f"{tool_name}.md",
    ]
    tool_file = None
    for c in candidates:
        if c.exists():
            tool_file = c
            break
    
    if not tool_file:
        return f"{tool_name}: tool file not found"
    
    params_file = PARAMS_DIR / f"{tool_name}.json"
    if not params_file.exists():
        return f"{tool_name}: no parsed_params"
    
    with open(params_file) as f:
        all_params = json.load(f)
    
    if not all_params:
        return f"{tool_name}: empty params"
    
    # Read the file
    text = tool_file.read_text()
    lines = text.split('\n')
    
    # Find the parameters section
    # Look for "  parameters:" in the frontmatter
    params_start = None
    params_end = None
    
    # We need to find the parameters: line in the frontmatter
    # The frontmatter ends with ---
    fm_end = 0
    if lines[0].strip() == '---':
        fm_end = 1
        while fm_end < len(lines) and lines[fm_end].strip() != '---':
            fm_end += 1
    
    for i in range(fm_end):
        if re.match(r'^\s*parameters:', lines[i]):
            params_start = i
            break
    
    if params_start is None:
        return f"{tool_name}: no parameters section in frontmatter"
    
    # Find the end of the parameters section (next top-level key or end of frontmatter)
    params_indent = len(lines[params_start]) - len(lines[params_start].lstrip())
    params_end = params_start + 1
    while params_end < fm_end:
        line = lines[params_end]
        # A new top-level key at the same indentation level as `parameters:`
        if line.strip() and len(line) - len(line.lstrip()) <= params_indent and ':' in line and line.split(':')[0].strip():
            # Check if it's another top-level key (not a dash line continuing parameters)
            stripped = line.strip()
            if not stripped.startswith('-') and not stripped.startswith('"') and len(stripped.split(':')) >= 2:
                # This is a new top-level key
                break
        params_end += 1
    
    # Collect existing param names
    existing_names = set()
    i = params_start + 1
    while i < params_end:
        name = param_name_from_yaml(lines[i])
        if name:
            existing_names.add(name)
        i += 1
    
    # Find missing params
    missing = [p for p in all_params if p['name'] not in existing_names]
    if not missing:
        return None  # No update needed
    
    # Find insertion point — end of parameters section
    insert_line = params_end
    
    # Generate YAML for missing params
    new_lines = []
    for p in missing:
        new_lines.append(param_to_yaml(p))
    
    # Insert new lines before the closing --- or next top-level key
    result_lines = lines[:insert_line] + [''] + new_lines + [''] + lines[insert_line:]
    
    tool_file.write_text('\n'.join(result_lines))
    return f"{tool_name}: added {len(missing)} params (was {len(existing_names)}, now {len(existing_names) + len(missing)})"

# Main
updated = 0
skipped = 0
errors = []
total = 0

for fpath in sorted(PARAMS_DIR.glob("*.json")):
    tool = fpath.stem
    total += 1
    result = update_tool_file(tool)
    if result and 'added' in result:
        updated += 1
        print(result)
    elif result:
        errors.append(result)
    else:
        skipped += 1

print(f"\n=== Summary ===")
print(f"Total tools with parsed_params: {total}")
print(f"Updated: {updated}")
print(f"Skipped (no gaps): {skipped}")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors[:10]:
        print(f"  {e}")
