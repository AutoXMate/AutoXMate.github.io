---
trust_level: community
id: windows-dllhijack-dbgmodel
namespace: windows:dllhijack:dbgmodel
name: dbgmodel.dll
description: "dbgmodel.dll — Sideloading hijacking (Microsoft)"
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
  template: "dbgmodel.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dbgmodel.html"
---
examples:
  - description: "Place malicious dbgmodel.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dbgmodel.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\Debuggers\\%VERSION%\\ntsd.exe\""

# dbgmodel.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\Debuggers\%VERSION%\ntsd.exe (Sideloading)
