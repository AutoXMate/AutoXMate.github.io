---
trust_level: community
id: windows-dllhijack-fxsapi
namespace: windows:dllhijack:fxsapi
name: fxsapi.dll
description: "fxsapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "fxsapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fxsapi.html"
---
examples:
  - description: "Place malicious fxsapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fxsapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fxsunatd.exe\""

# fxsapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fxsunatd.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
