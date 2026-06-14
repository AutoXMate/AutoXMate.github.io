---
trust_level: community
id: windows-dllhijack-tapi32
namespace: windows:dllhijack:tapi32
name: tapi32.dll
description: tapi32.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
- security.privilegeescalation.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
- privilege-escalation
execution:
  template: tapi32.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/tapi32.html
features:
- requires-root
---

examples:
  - description: "Place malicious tapi32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tapi32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dialer.exe\""

# tapi32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dialer.exe (Sideloading)
- %SYSTEM32%\fxssvc.exe (Sideloading)
- %SYSTEM32%\tcmsetup.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
