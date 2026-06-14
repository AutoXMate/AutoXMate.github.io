---
trust_level: community
id: windows-dllhijack-nshhttp
namespace: windows:dllhijack:nshhttp
name: nshhttp.dll
description: nshhttp.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: nshhttp.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/nshhttp.html
features:
- network-intensive
---

examples:
  - description: "Place malicious nshhttp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\nshhttp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# nshhttp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
