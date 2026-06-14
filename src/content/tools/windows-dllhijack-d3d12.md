---
trust_level: community
id: windows-dllhijack-d3d12
namespace: windows:dllhijack:d3d12
name: d3d12.dll
description: "d3d12.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "d3d12.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/d3d12.html"
---
examples:
  - description: "Place malicious d3d12.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d3d12.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dxgiadaptercache.exe\""

# d3d12.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dxgiadaptercache.exe (Sideloading)
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
