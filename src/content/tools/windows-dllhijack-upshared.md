---
trust_level: community
id: windows-dllhijack-upshared
namespace: windows:dllhijack:upshared
name: upshared.dll
description: upshared.dll — Sideloading hijacking (Microsoft)
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
  template: upshared.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/upshared.html
features:
- process-manip
---

examples:
  - description: "Place malicious upshared.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\upshared.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\musnotification.exe\""

# upshared.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\musnotifyicon.exe (Sideloading)

**Acknowledgement:** Wietze
