---
trust_level: community
id: windows-dllhijack-bootmenuux
namespace: windows:dllhijack:bootmenuux
name: bootmenuux.dll
description: "bootmenuux.dll — Sideloading hijacking (Microsoft)"
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
  template: "bootmenuux.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bootmenuux.html"
---
examples:
  - description: "Place malicious bootmenuux.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bootmenuux.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# bootmenuux.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)

**Acknowledgement:** Wietze
