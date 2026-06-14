---
trust_level: community
id: windows-dllhijack-aepic
namespace: windows:dllhijack:aepic
name: aepic.dll
description: "aepic.dll — Sideloading hijacking (Microsoft)"
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
  template: "aepic.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/aepic.html"
---
examples:
  - description: "Place malicious aepic.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\aepic.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\psr.exe\""

# aepic.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\psr.exe (Sideloading)

**Acknowledgement:** Wietze
