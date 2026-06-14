---
trust_level: community
id: windows-dllhijack-reseteng
namespace: windows:dllhijack:reseteng
name: reseteng.dll
description: "reseteng.dll — Sideloading hijacking (Microsoft)"
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
  template: "reseteng.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/reseteng.html"
---
examples:
  - description: "Place malicious reseteng.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\reseteng.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# reseteng.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)

**Acknowledgement:** Wietze
