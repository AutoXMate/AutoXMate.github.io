---
trust_level: community
id: windows-dllhijack-rcdll
namespace: windows:dllhijack:rcdll
name: rcdll.dll
description: "rcdll.dll — Sideloading hijacking (Microsoft)"
author: "Gary Lobermier"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "rcdll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rcdll.html"
---
examples:
  - description: "Place malicious rcdll.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\10\\bin\\%VERSION%\\%VERSION%\\rcdll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\bin\\%VERSION%\\%VERSION%\\rc.exe\""

# rcdll.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\%VERSION%\rc.exe (Sideloading)
