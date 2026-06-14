---
trust_level: community
id: windows-dllhijack-magnification
namespace: windows:dllhijack:magnification
name: magnification.dll
description: magnification.dll — Sideloading hijacking (Microsoft)
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
  template: magnification.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/magnification.html
features:
- pipes-stdout
---

examples:
  - description: "Place malicious magnification.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\magnification.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\magnify.exe\""

# magnification.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\magnify.exe (Sideloading)

**Acknowledgement:** Wietze
