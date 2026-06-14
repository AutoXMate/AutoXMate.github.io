---
trust_level: community
id: windows-dllhijack-bderepair
namespace: windows:dllhijack:bderepair
name: bderepair.dll
description: "bderepair.dll — Sideloading hijacking (Microsoft)"
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
  template: "bderepair.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bderepair.html"
---
examples:
  - description: "Place malicious bderepair.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bderepair.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\repair-bde.exe\""

# bderepair.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\repair-bde.exe (Sideloading)

**Acknowledgement:** Wietze
