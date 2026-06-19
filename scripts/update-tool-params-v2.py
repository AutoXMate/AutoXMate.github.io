#!/usr/bin/env python3
"""
Fix YAML parameter sections across all tool files damaged by the initial update.
Handles both `parameters:` and `parameters: []` syntax, and detects the 
indentation scheme used in each file.
"""
import re, json, os, sys
from pathlib import Path

TOOLS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools")
PARAMS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/data/parsed_params")

def indent_of(line):
    return len(line) - len(line.lstrip())

def param_alias(param):
    """Get the normalized flag alias for comparison."""
    aliases = param.get('aliases', [])
    return aliases[0].split()[0].strip() if aliases else f"--{param['name'].replace('_', '-')}"

def main():
    # Step 1: Find all damaged files (has `parameters: []` followed by any indented name: or - name: line)
    # Also find files where appended entries don't match the original indent pattern
    param_names_re = re.compile(r'^\s*- name:\s*(.+)')
    
    for fpath in sorted(TOOLS_DIR.glob("*.md")):
        text = fpath.read_text()
        lines = text.split('\n')
        
        # Find frontmatter boundaries
        if not lines or lines[0].strip() != '---':
            continue
        fm_end = 1
        while fm_end < len(lines) and lines[fm_end].strip() != '---':
            fm_end += 1
        
        # Find parameters: line
        params_li = None
        params_indent = 0
        for i in range(1, fm_end):
            m = re.match(r'^(\s*)parameters:', lines[i])
            if m:
                params_li = i
                params_indent = len(m.group(1))
                break
        
        if params_li is None:
            continue
        
        params_line = lines[params_li]
        
        # Check if this is the inline `[]` form
        is_inline = '[' in params_line
        
        # Find end of parameters section
        section_end = params_li + 1
        while section_end < fm_end:
            line = lines[section_end]
            if line.strip() and indent_of(line) <= params_indent:
                # Check if this is a new top-level key (not continuing the parameter list)
                stripped = line.strip()
                if not stripped.startswith('-') and not stripped.startswith('"') and ':' in stripped:
                    potential_key = stripped.split(':')[0].strip()
                    # Don't break on property-like keys that are deeper than the parameters indent
                    if indent_of(line) == params_indent:
                        # It's at the same level as `parameters:` — a new top-level key
                        break
            section_end += 1
        
        # Collect existing param names that are in the parameters section
        existing_names = set()
        existing_flagnames = set()
        for i in range(params_li + 1, section_end):
            m = param_names_re.match(lines[i])
            if m:
                name = m.group(1).strip()
                existing_names.add(name)
        
        # Load params from parsed_params
        tool_name = fpath.stem
        params_file = PARAMS_DIR / f"{tool_name}.json"
        if not params_file.exists():
            continue
        all_params = json.loads(params_file.read_text())
        if not all_params:
            continue
        
        # Find missing params
        missing = [p for p in all_params if p['name'] not in existing_names]
        if not missing:
            continue
        
        # === Generate YAML for missing params ===
        # Detect the indentation scheme — only count the FIRST `- name:` item
        # (to avoid being confused by nested lists like aliases)
        first_name_indent = None
        for i in range(params_li + 1, min(section_end, params_li + 50)):
            line = lines[i]
            m2 = re.match(r'^(\s*)- name:', line)
            if m2:
                first_name_indent = len(m2.group(1))
                break
        
        if first_name_indent is not None:
            list_indent = first_name_indent
        else:
            list_indent = params_indent + 2
        
        # Property indent is list_indent + 2 (conventional)
        prop_indent = list_indent + 2
        
        def param_to_yaml_lines(p, list_indent, prop_indent):
            """Generate YAML lines for a parameter entry."""
            lines_out = []
            prefix = " " * list_indent + "- "
            prop = " " * prop_indent
            
            # Always quote the name in case it's a YAML reserved word or number
            name_val = p['name']
            if not (name_val.startswith('"') and name_val.endswith('"')):
                name_val = f"\"{name_val}\""
            lines_out.append(f"{prefix}name: {name_val}")
            
            type_str = p.get('type', 'boolean')
            if p.get('has_arg'):
                type_str = 'arg'
            lines_out.append(f"{prop}type: {type_str}")
            lines_out.append(f"{prop}required: {'true' if p.get('required') else 'false'}")
            
            if type_str != 'boolean':
                default = p.get('default_value', '')
                lines_out.append(f"{prop}default: {default if default else 'null'}")
            
            desc = p.get('description', '').replace('"', '\\"')
            lines_out.append(f'{prop}description: "{desc}"')
            
            aliases = [a for a in p.get('aliases', []) if a.strip() and a.startswith('-')]
            if aliases:
                lines_out.append(f"{prop}aliases:")
                for alias in aliases:
                    lines_out.append(f"{' ' * (prop_indent + 2)}- \"{alias}\"")
            
            return lines_out
        
        # Generate missing param YAML
        new_lines = []
        # Force consistent indentation matching the existing style
        for p in missing:
            new_lines.extend(param_to_yaml_lines(p, list_indent, prop_indent))
        
        if not new_lines:
            continue
        
        # === Apply changes ===
        # Case 1: Inline `parameters: []` — need to convert
        if is_inline:
            # Replace `parameters: []` with `parameters:` 
            lines[params_li] = f"{' ' * params_indent}parameters:"
            # Remove the `]` part if on the same line — already handled
            # Insert missing params after the `parameters:` line
            insert_at = params_li + 1
            # Skip any existing content that was under `parameters: []`
            # (there shouldn't be any valid content there, but just in case)
            while insert_at < section_end:
                if lines[insert_at].strip():
                    break
                insert_at += 1
            
            # Remove old empty lines between parameters: and next key
            # by inserting new lines at the right spot
            result = lines[:insert_at] + [''] + new_lines + [''] + lines[section_end:]
        else:
            # Case 2: Normal block parameters — append after the last param entry
            # Insert before the next top-level key (section_end)
            result = lines[:section_end] + [''] + new_lines + [''] + lines[section_end:]
        
        fpath.write_text('\n'.join(result))
        existing_count = len(existing_names)
        print(f"{fpath.stem:35s}: added {len(missing):3d} params (was {existing_count:3d}, now {existing_count + len(missing):3d}) [{is_inline=}, {list_indent=}]")

if __name__ == '__main__':
    main()
