---
trust_level: community
id: windows-dllhijack-winipsec
namespace: windows:dllhijack:winipsec
name: winipsec.dll
description: winipsec.dll — Sideloading hijacking (Microsoft)
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
  template: winipsec.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/winipsec.html
features:
- process-manip
---

examples:
  - description: "Place malicious winipsec.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winipsec.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# winipsec.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
