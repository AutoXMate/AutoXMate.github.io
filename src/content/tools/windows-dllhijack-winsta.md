---
trust_level: community
id: windows-dllhijack-winsta
namespace: windows:dllhijack:winsta
name: winsta.dll
description: winsta.dll — Sideloading hijacking (Microsoft)
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
  template: winsta.dll
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
  url: https://twitter.com/BSummerz/status/1716851156625105342
- label: HijackLibs
  url: https://hijacklibs.net/entries/winsta.html
features:
- requires-root
---

examples:
  - description: "Place malicious winsta.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winsta.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\change.exe\""

# winsta.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\change.exe (Sideloading)
- %SYSTEM32%\chglogon.exe (Sideloading)
- %SYSTEM32%\chgport.exe (Sideloading)
- %SYSTEM32%\ctfmon.exe (Sideloading)
- %SYSTEM32%\displayswitch.exe (Sideloading)
- %SYSTEM32%\msg.exe (Sideloading)
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\query.exe (Sideloading)
- %SYSTEM32%\quser.exe (Sideloading)
- %SYSTEM32%\qprocess.exe (Sideloading)
- %SYSTEM32%\qwinsta.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\rdpinput.exe (Sideloading)
- %SYSTEM32%\rdpsa.exe (Sideloading)
- %SYSTEM32%\rdpsauachelper.exe (Sideloading)
- %SYSTEM32%\rdpshell.exe (Sideloading)
- %SYSTEM32%\rdvghelper.exe (Sideloading)
- %SYSTEM32%\reset.exe (Sideloading)
- %SYSTEM32%\rwinsta.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiescomputername.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesdataexecutionprevention.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertieshardware.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesprotection.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systempropertiesremote.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tscon.exe (Sideloading)
- %SYSTEM32%\tsdiscon.exe (Sideloading)
- %SYSTEM32%\tskill.exe (Sideloading)
- %SYSTEM32%\DriverStore\FileRepository\%VERSION%\igfxSDK.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Will Summerhill
