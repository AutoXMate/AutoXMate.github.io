---
trust_level: community
id: windows-dllhijack-oleacc
namespace: windows:dllhijack:oleacc
name: oleacc.dll
description: oleacc.dll — Sideloading hijacking (Microsoft)
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
  template: oleacc.dll
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
  url: https://hijacklibs.net/entries/oleacc.html
features:
- requires-root
---

examples:
  - description: "Place malicious oleacc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\oleacc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# oleacc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\cttune.exe (Sideloading)
- %SYSTEM32%\devicepairingwizard.exe (Sideloading)
- %SYSTEM32%\easeofaccessdialog.exe (Sideloading)
- %SYSTEM32%\fsquirt.exe (Sideloading)
- %SYSTEM32%\magnify.exe (Sideloading)
- %SYSTEM32%\optionalfeatures.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\sethc.exe (Sideloading)
- %SYSTEM32%\snippingtool.exe (Sideloading)
- %SYSTEM32%\utilman.exe (Sideloading)
- %SYSTEM32%\wmpdmc.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
