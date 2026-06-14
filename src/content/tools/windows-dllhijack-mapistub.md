---
trust_level: community
id: windows-dllhijack-mapistub
namespace: windows:dllhijack:mapistub
name: mapistub.dll
description: "mapistub.dll — Sideloading hijacking (Microsoft)"
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
  template: "mapistub.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mapistub.html"
---
examples:
  - description: "Place malicious mapistub.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mapistub.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fixmapi.exe\""

# mapistub.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fixmapi.exe (Sideloading)

**Acknowledgement:** Wietze
