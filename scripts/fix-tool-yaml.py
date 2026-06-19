#!/usr/bin/env python3
"""
Validate and fix all tool YAML frontmatter for common issues:
- Unescaped special characters in descriptions
- Trailing quotes in flags/aliases
- Invalid boolean default values
- Unquoted strings with risky characters
"""
import re, sys, yaml
from pathlib import Path

TOOLS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools")

def fix_yaml_file(fpath):
    """Parse, fix, and re-serialize YAML frontmatter preserving content order."""
    text = fpath.read_text()
    lines = text.split('\n')
    
    # Find frontmatter
    if not lines or lines[0].strip() != '---':
        return None
    
    fm_end = 1
    while fm_end < len(lines) and lines[fm_end].strip() != '---':
        fm_end += 1
    
    if fm_end >= len(lines):
        return None
    
    # Parse frontmatter YAML
    fm_text = '\n'.join(lines[1:fm_end])
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return f"YAML error: {e}"
    
    if not data or 'parameters' not in data:
        return None
    
    params = data['parameters']
    if not params:
        return None
    
    fixed_count = 0
    for param in params:
        # Fix description
        if 'description' in param and isinstance(param['description'], str):
            desc = param['description']
            # Remove trailing ` or ' that might come from help text parsing
            desc = desc.rstrip('`\'"')
            # Ensure proper quoting
            if any(c in desc for c in ['~', '!', '#', '@', '&', '*', '?', '|', '>', '<', '{', '}', '[', ']', ':', '`', '"', "'"]):
                if not (desc.startswith('"') and desc.endswith('"')):
                    pass  # yaml.safe_dump will handle this
            param['description'] = desc
        
        # Fix default_value
        if 'default_value' in param:
            dv = param['default_value']
            if isinstance(dv, str):
                # Remove quoting artifacts
                dv = dv.strip('`\'"')
                if dv in ('~', 'null', 'None', '') or not dv:
                    del param['default_value']
                    param['default'] = None
                elif dv.isdigit():
                    param['default'] = int(dv)
                else:
                    param['default'] = dv
                fixed_count += 1
            del param['default_value']
        elif 'default' in param:
            dv = param['default']
            if isinstance(dv, str):
                dv = dv.strip('`\'"')
                if dv in ('~', 'null', 'None', '') or not dv:
                    param['default'] = None
                else:
                    param['default'] = dv
        
        # Fix aliases
        if 'aliases' in param:
            cleaned = []
            for alias in param['aliases']:
                if isinstance(alias, str):
                    alias = alias.strip('`"\'')
                    if alias and alias.startswith('-'):
                        cleaned.append(alias)
            param['aliases'] = cleaned
        
        # Fix booleans
        if param.get('type') == 'boolean' and 'default' in param:
            if param['default'] in ('true', 'True', 'TRUE', 1, '1'):
                param['default'] = True
            elif param['default'] in ('false', 'False', 'FALSE', 0, '0', None, 'null'):
                del param['default']
        elif param.get('type') != 'boolean' and 'default' in param:
            if param['default'] in (None, 'null', '~'):
                del param['default']
    
    # Re-serialize
    fixed_fm = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120, indent=2)
    
    # Reconstruct file
    fixed_text = '---\n' + fixed_fm + '---\n' + '\n'.join(lines[fm_end+1:])
    
    if fixed_text == text:
        return None
    
    fpath.write_text(fixed_text)
    return f"Fixed"

def main():
    fixed = 0
    errors = []
    for fpath in sorted(TOOLS_DIR.glob("*.md")):
        result = fix_yaml_file(fpath)
        if result == "Fixed":
            fixed += 1
            print(f"  {fpath.stem}")
        elif result:
            errors.append(f"{fpath.stem}: {result}")
    
    print(f"\nFixed: {fixed}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors[:10]:
            print(f"  {e}")

if __name__ == '__main__':
    main()
