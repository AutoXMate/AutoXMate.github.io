---
trust_level: community
id: windows-dllhijack-wdscore
namespace: windows:dllhijack:wdscore
name: wdscore.dll
description: wdscore.dll — Sideloading hijacking (Microsoft)
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
  template: wdscore.dll
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
- label: Reference
  url: https://www.hexacorn.com/blog/2023/12/30/1-little-known-secret-of-ieunatt-exe-on-win11/
- label: HijackLibs
  url: https://hijacklibs.net/entries/wdscore.html
features:
- requires-root
---

examples:
  - description: "Place malicious wdscore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wdscore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# wdscore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\deploymentcsphelper.exe (Sideloading)
- %SYSTEM32%\djoin.exe (Sideloading)
- %SYSTEM32%\dnscacheugc.exe (Sideloading)
- %SYSTEM32%\muiunattend.exe (Sideloading)
- %SYSTEM32%\netbtugc.exe (Sideloading)
- %SYSTEM32%\netiougc.exe (Sideloading)
- %SYSTEM32%\pnpunattend.exe (Sideloading)
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\setupugc.exe (Sideloading)
- %SYSTEM32%\sysreseterr.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tapiunattend.exe (Sideloading)
- %SYSTEM32%\ieunatt.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Adam
