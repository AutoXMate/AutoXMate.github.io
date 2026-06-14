---
trust_level: community
id: windows-dllhijack-wevtapi
namespace: windows:dllhijack:wevtapi
name: wevtapi.dll
description: wevtapi.dll — Sideloading, Environment Variable hijacking (Microsoft)
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
  template: wevtapi.dll
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
  url: https://hijacklibs.net/entries/wevtapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious wevtapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wevtapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cidiag.exe\""

# wevtapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cidiag.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\gpupdate.exe (Sideloading)
- %SYSTEM32%\mbaeparsertask.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\nlb.exe (Sideloading)
- %SYSTEM32%\packageinspector.exe (Sideloading)
- %SYSTEM32%\plasrv.exe (Sideloading)
- %SYSTEM32%\tracerpt.exe (Sideloading)
- %SYSTEM32%\wecutil.exe (Sideloading)
- %SYSTEM32%\wlbs.exe (Sideloading)
- %SYSTEM32%\wsreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\logman.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
