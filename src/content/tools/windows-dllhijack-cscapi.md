---
trust_level: community
id: windows-dllhijack-cscapi
namespace: windows:dllhijack:cscapi
name: cscapi.dll
description: "cscapi.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "cscapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cscapi.html"
---
examples:
  - description: "Place malicious cscapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cscapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# cscapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\microsoft.uev.cscunpintool.exe (Sideloading)

**Acknowledgement:** Wietze
