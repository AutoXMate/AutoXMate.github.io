---
trust_level: community
id: windows-dllhijack-duser
namespace: windows:dllhijack:duser
name: duser.dll
description: duser.dll — Sideloading hijacking (Microsoft)
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
  template: duser.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://twitter.com/0xcarnage/status/1203882560176218113
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/duser.html
features:
- requires-root
---

examples:
  - description: "Place malicious duser.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\duser.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bdeunlock.exe\""

# duser.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bdeunlock.exe (Sideloading)
- %SYSTEM32%\displayswitch.exe (Sideloading)
- %SYSTEM32%\easeofaccessdialog.exe (Sideloading)
- %SYSTEM32%\lockscreencontentserver.exe (Sideloading)
- %SYSTEM32%\mmc.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\sessionmsg.exe (Sideloading)
- %SYSTEM32%\taskmgr.exe (Sideloading)
- %SYSTEM32%\utilman.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
