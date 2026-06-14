---
trust_level: community
id: windows-dllhijack-bcd
namespace: windows:dllhijack:bcd
name: bcd.dll
description: bcd.dll — Sideloading hijacking (Microsoft)
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
  template: bcd.dll
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
  url: https://hijacklibs.net/entries/bcd.html
features:
- requires-root
---

examples:
  - description: "Place malicious bcd.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bcd.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# bcd.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\cidiag.exe (Sideloading)
- %SYSTEM32%\genvalobj.exe (Sideloading)
- %SYSTEM32%\mdsched.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\msconfig.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\recdisc.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\rstrui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\srtasks.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiescomputername.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesdataexecutionprevention.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertieshardware.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesprotection.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesremote.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\vds.exe (Sideloading)
- %SYSTEM32%\vdsldr.exe (Sideloading)
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
