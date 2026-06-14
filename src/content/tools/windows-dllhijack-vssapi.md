---
trust_level: community
id: windows-dllhijack-vssapi
namespace: windows:dllhijack:vssapi
name: vssapi.dll
description: vssapi.dll — Sideloading hijacking (Microsoft)
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
  template: vssapi.dll
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
  url: https://www.welivesecurity.com/2023/03/14/slow-ticking-time-bomb-tick-apt-group-dlp-software-developer-east-asia/
- label: HijackLibs
  url: https://hijacklibs.net/entries/vssapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious vssapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\vssapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# vssapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\cleanmgr.exe (Sideloading)
- %SYSTEM32%\dsdbutil.exe (Sideloading)
- %SYSTEM32%\ntdsutil.exe (Sideloading)
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\rstrui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\srtasks.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\vssadmin.exe (Sideloading)
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)
- %PROGRAMFILES%\Avira\Antivirus\avshadow.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
