---
trust_level: community
id: windows-dllhijack-dxva2
namespace: windows:dllhijack:dxva2
name: dxva2.dll
description: "dxva2.dll — Sideloading hijacking (Microsoft)"
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
  template: "dxva2.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dxva2.html"
---
examples:
  - description: "Place malicious dxva2.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dxva2.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dccw.exe\""

# dxva2.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dccw.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\dispdiag.exe (Sideloading)

**Acknowledgement:** Wietze
