---
trust_level: community
id: windows-dllhijack-d3d9
namespace: windows:dllhijack:d3d9
name: d3d9.dll
description: "d3d9.dll — Sideloading hijacking (Microsoft)"
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
  template: "d3d9.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/d3d9.html"
---
examples:
  - description: "Place malicious d3d9.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d3d9.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\magnify.exe\""

# d3d9.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\magnify.exe (Sideloading)

**Acknowledgement:** Wietze
