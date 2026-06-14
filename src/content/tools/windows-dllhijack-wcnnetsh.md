---
trust_level: community
id: windows-dllhijack-wcnnetsh
namespace: windows:dllhijack:wcnnetsh
name: wcnnetsh.dll
description: "wcnnetsh.dll — Sideloading hijacking (Microsoft)"
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
  template: "wcnnetsh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wcnnetsh.html"
---
examples:
  - description: "Place malicious wcnnetsh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wcnnetsh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# wcnnetsh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
