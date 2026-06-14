---
trust_level: community
id: windows-dllhijack-python39
namespace: windows:dllhijack:python39
name: python39.dll
description: python39.dll — Sideloading hijacking (Python)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: python39.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://twitter.com/SBousseaden/status/1530595156055011330
- label: HijackLibs
  url: https://hijacklibs.net/entries/python39.html
features:
- interactive
---

examples:
  - description: "Place malicious python39.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Python39\\python39.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"python39.exe\""

# python39.dll

**Vendor:** Python

**Expected Location:** %PROGRAMFILES%\Python39

**Vulnerable Executables:**
- python39.exe (Sideloading)

**Acknowledgement:** Samir
