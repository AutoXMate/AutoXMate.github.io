---
trust_level: community
id: windows-dllhijack-mprapi
namespace: windows:dllhijack:mprapi
name: mprapi.dll
description: "mprapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "mprapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mprapi.html"
---
examples:
  - description: "Place malicious mprapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mprapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rasautou.exe\""

# mprapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rasautou.exe (Sideloading)

**Acknowledgement:** Wietze
