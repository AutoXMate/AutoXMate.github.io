---
trust_level: community
id: windows-dllhijack-resetengine
namespace: windows:dllhijack:resetengine
name: resetengine.dll
description: "resetengine.dll — Sideloading hijacking (Microsoft)"
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
  template: "resetengine.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/resetengine.html"
---
examples:
  - description: "Place malicious resetengine.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\resetengine.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\resetengine.exe\""

# resetengine.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
