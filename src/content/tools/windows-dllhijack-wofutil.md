---
trust_level: community
id: windows-dllhijack-wofutil
namespace: windows:dllhijack:wofutil
name: wofutil.dll
description: wofutil.dll — Sideloading hijacking (Microsoft)
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
  template: wofutil.dll
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
  url: https://hijacklibs.net/entries/wofutil.html
features:
- requires-root
---

examples:
  - description: "Place malicious wofutil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wofutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\recoverydrive.exe\""

# wofutil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
