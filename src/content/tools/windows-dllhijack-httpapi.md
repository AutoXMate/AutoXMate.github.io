---
trust_level: community
id: windows-dllhijack-httpapi
namespace: windows:dllhijack:httpapi
name: httpapi.dll
description: httpapi.dll — Sideloading hijacking (Microsoft)
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
  template: httpapi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/httpapi.html
features:
- network-intensive
---

examples:
  - description: "Place malicious httpapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\httpapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# httpapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\wifitask.exe (Sideloading)
- %SYSTEM32%\wsmanhttpconfig.exe (Sideloading)

**Acknowledgement:** Wietze
