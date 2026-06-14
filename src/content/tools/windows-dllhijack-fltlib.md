---
trust_level: community
id: windows-dllhijack-fltlib
namespace: windows:dllhijack:fltlib
name: fltlib.dll
description: fltlib.dll — Sideloading hijacking (Microsoft)
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
  template: fltlib.dll
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
  url: https://hijacklibs.net/entries/fltlib.html
features:
- requires-root
---

examples:
  - description: "Place malicious fltlib.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fltlib.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\agentservice.exe\""

# fltlib.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\agentservice.exe (Sideloading)
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Sideloading)
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\fltmc.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\resmon.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
