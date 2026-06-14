---
trust_level: community
id: windows-dllhijack-p2pnetsh
namespace: windows:dllhijack:p2pnetsh
name: p2pnetsh.dll
description: "p2pnetsh.dll — Sideloading hijacking (Microsoft)"
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
  template: "p2pnetsh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/p2pnetsh.html"
---
examples:
  - description: "Place malicious p2pnetsh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\p2pnetsh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# p2pnetsh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
