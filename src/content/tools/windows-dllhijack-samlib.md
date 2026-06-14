---
trust_level: community
id: windows-dllhijack-samlib
namespace: windows:dllhijack:samlib
name: samlib.dll
description: samlib.dll — Sideloading hijacking (Microsoft)
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
  template: samlib.dll
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
  url: https://hijacklibs.net/entries/samlib.html
features:
- requires-root
---

examples:
  - description: "Place malicious samlib.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\samlib.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dpapimig.exe\""

# samlib.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dpapimig.exe (Sideloading)
- %SYSTEM32%\dsmgmt.exe (Sideloading)
- %SYSTEM32%\easinvoker.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\netplwiz.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\ntdsutil.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
