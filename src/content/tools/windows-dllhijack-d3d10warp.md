---
trust_level: community
id: windows-dllhijack-d3d10warp
namespace: windows:dllhijack:d3d10warp
name: d3d10warp.dll
description: "d3d10warp.dll — Sideloading hijacking (Microsoft)"
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
  template: "d3d10warp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/d3d10warp.html"
---
examples:
  - description: "Place malicious d3d10warp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d3d10warp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\slidetoshutdown.exe\""

# d3d10warp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\slidetoshutdown.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
