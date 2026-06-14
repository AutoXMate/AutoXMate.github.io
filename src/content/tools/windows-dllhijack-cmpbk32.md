---
trust_level: community
id: windows-dllhijack-cmpbk32
namespace: windows:dllhijack:cmpbk32
name: cmpbk32.dll
description: "cmpbk32.dll — Sideloading hijacking (Microsoft)"
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
  template: "cmpbk32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cmpbk32.html"
---
examples:
  - description: "Place malicious cmpbk32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cmpbk32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cmdl32.exe\""

# cmpbk32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cmdl32.exe (Sideloading)

**Acknowledgement:** Wietze
