---
trust_level: community
id: windows-dllhijack-samcli
namespace: windows:dllhijack:samcli
name: samcli.dll
description: samcli.dll — Sideloading hijacking (Microsoft)
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
  template: samcli.dll
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
  url: https://hijacklibs.net/entries/samcli.html
features:
- requires-root
---

examples:
  - description: "Place malicious samcli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\samcli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certutil.exe\""

# samcli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\change.exe (Sideloading)
- %SYSTEM32%\chglogon.exe (Sideloading)
- %SYSTEM32%\chgport.exe (Sideloading)
- %SYSTEM32%\credwiz.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dpapimig.exe (Sideloading)
- %SYSTEM32%\easinvoker.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\net.exe (Sideloading)
- %SYSTEM32%\net1.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\netplwiz.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\query.exe (Sideloading)
- %SYSTEM32%\quser.exe (Sideloading)
- %SYSTEM32%\qwinsta.exe (Sideloading)
- %SYSTEM32%\raserver.exe (Sideloading)
- %SYSTEM32%\reset.exe (Sideloading)
- %SYSTEM32%\rwinsta.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tscon.exe (Sideloading)
- %SYSTEM32%\tskill.exe (Sideloading)
- %SYSTEM32%\wpcmon.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
