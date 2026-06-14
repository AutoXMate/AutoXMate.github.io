---
trust_level: community
id: windows-dllhijack-classicexplorer32
namespace: windows:dllhijack:classicexplorer32
name: classicexplorer32.dll
description: classicexplorer32.dll — Sideloading hijacking (Classic Shell)
author: Pokhlebin Maxim
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: classicexplorer32.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://blogs.blackberry.com/en/2022/12/mustang-panda-uses-the-russian-ukrainian-war-to-attack-europe-and-asia-pacific-targets
- label: HijackLibs
  url: https://hijacklibs.net/entries/classicexplorer32.html
features:
- interactive
---

examples:
  - description: "Place malicious classicexplorer32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Classic Shell\\classicexplorer32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"ClassicExplorerSettings.exe\""

# classicexplorer32.dll

**Vendor:** Classic Shell

**Expected Location:** %PROGRAMFILES%\Classic Shell

**Vulnerable Executables:**
- ClassicExplorerSettings.exe (Sideloading)
