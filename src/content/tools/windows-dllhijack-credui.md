---
trust_level: community
id: windows-dllhijack-credui
namespace: windows:dllhijack:credui
name: credui.dll
description: credui.dll — Sideloading, Environment Variable hijacking (Microsoft)
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
  template: credui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/credui.html
features:
- requires-root
---

examples:
  - description: "Place malicious credui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\credui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\efsui.exe\""

# credui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\fxssvc.exe (Sideloading)
- %SYSTEM32%\gpfixup.exe (Sideloading)
- %SYSTEM32%\licmgr.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\nlbmgr.exe (Sideloading)
- %SYSTEM32%\perfmon.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\rpcping.exe (Sideloading)
- %SYSTEM32%\runas.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wbadmin.exe (Sideloading)
- %SYSTEM32%\wfs.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
