#!/usr/bin/env python3
"""Check frontmatter delimiters."""
import sys

# Check existing tool
existing_path = "/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools/curl.md"
with open(existing_path) as f:
    text = f.read()

parts = text.split('---', 2)
print(f"curl.md: {len(parts)} parts")
if len(parts) >= 2:
    print(f"  Part 0: {repr(parts[0][:20])}")
    print(f"  Part 1: {repr(parts[1][:50])}")
    print(f"  File ends: {repr(text[-80:])}")
    print(f"  Has closing ---: {'---' in parts[2] if len(parts) > 2 else 'N/A'}")

# Check a new tool
new_path = "/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools/bcdedit.md"
with open(new_path) as f:
    text = f.read()

parts = text.split('---', 2)
print(f"\nbcdedit.md: {len(parts)} parts")
if len(parts) >= 2:
    print(f"  Part 0: {repr(parts[0][:20])}")
    print(f"  Part 1: {repr(parts[1][:50])}")
    print(f"  File ends: {repr(text[-80:])}")
    print(f"  Has closing ---: {'---' in parts[2] if len(parts) > 2 else parts[1][-30:]}")
