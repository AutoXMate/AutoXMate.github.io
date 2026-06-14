---
trust_level: community
id: windows-dllhijack-newdev
namespace: windows:dllhijack:newdev
name: newdev.dll
description: newdev.dll — Sideloading hijacking (Microsoft)
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
  template: newdev.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/newdev.html
features:
- requires-root
---

examples:
  - description: "Place malicious newdev.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\newdev.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\infdefaultinstall.exe\""

# newdev.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\infdefaultinstall.exe (Sideloading)
- %SYSTEM32%\pnpunattend.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
