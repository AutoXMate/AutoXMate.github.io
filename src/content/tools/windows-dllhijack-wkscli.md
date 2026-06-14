---
trust_level: community
id: windows-dllhijack-wkscli
namespace: windows:dllhijack:wkscli
name: wkscli.dll
description: wkscli.dll — Sideloading hijacking (Microsoft)
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
  template: wkscli.dll
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
  url: https://hijacklibs.net/entries/wkscli.html
features:
- requires-root
---

examples:
  - description: "Place malicious wkscli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wkscli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\djoin.exe\""

# wkscli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\djoin.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\getmac.exe (Sideloading)
- %SYSTEM32%\ie4uinit.exe (Sideloading)
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\net.exe (Sideloading)
- %SYSTEM32%\net1.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\secinit.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\whoami.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
