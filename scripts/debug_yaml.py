#!/usr/bin/env python3
"""Debug YAML parsing issue."""
import yaml
import sys

fails = ["bcdedit.md", "driverquery.md", "host.md", "systeminfo.md", "dir.md"]

for fname in fails:
    path = f"/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools/{fname}"
    with open(path) as f:
        text = f.read()
    
    parts = text.split('---', 2)
    print(f"=== {fname} ===")
    print(f"  Text length: {len(text)}")
    print(f"  Parts: {len(parts)}")
    if len(parts) >= 2:
        fm = parts[1]
        print(f"  FM length: {len(fm)}")
        print(f"  FM starts with: {repr(fm[:50])}")
        print(f"  FM ends with: {repr(fm[-50:])}")
        try:
            data = yaml.safe_load(fm)
            print(f"  ✓ Parsed OK: keys={list(data.keys())}")
        except Exception as e:
            print(f"  ✗ Parse error: {e}")
    else:
        print(f"  ✗ No frontmatter")
