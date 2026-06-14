---
trust_level: community
id: windows-dllhijack-dismapi
namespace: windows:dllhijack:dismapi
name: dismapi.dll
description: dismapi.dll — Sideloading hijacking (Microsoft)
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
  template: dismapi.dll
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
  url: https://hijacklibs.net/entries/dismapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious dismapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dismapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# dismapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\deploymentcsphelper.exe (Sideloading)
- %SYSTEM32%\directxdatabaseupdater.exe (Sideloading)
- %SYSTEM32%\hvsievaluator.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
