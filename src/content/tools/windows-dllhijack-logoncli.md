---
trust_level: community
id: windows-dllhijack-logoncli
namespace: windows:dllhijack:logoncli
name: logoncli.dll
description: "logoncli.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
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
  template: "logoncli.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/logoncli.html"
---
examples:
  - description: "Place malicious logoncli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\logoncli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certutil.exe\""

# logoncli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\change.exe (Sideloading)
- %SYSTEM32%\chglogon.exe (Sideloading)
- %SYSTEM32%\chgport.exe (Sideloading)
- %SYSTEM32%\csvde.exe (Sideloading)
- %SYSTEM32%\devicecensus.exe (Sideloading)
- %SYSTEM32%\djoin.exe (Sideloading)
- %SYSTEM32%\dsacls.exe (Sideloading)
- %SYSTEM32%\dsmgmt.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\gpfixup.exe (Sideloading)
- %SYSTEM32%\gpresult.exe (Sideloading)
- %SYSTEM32%\klist.exe (Sideloading)
- %SYSTEM32%\ksetup.exe (Sideloading)
- %SYSTEM32%\ldifde.exe (Sideloading)
- %SYSTEM32%\net1.exe (Sideloading)
- %SYSTEM32%\nltest.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\ntdsutil.exe (Sideloading)
- %SYSTEM32%\query.exe (Sideloading)
- %SYSTEM32%\quser.exe (Sideloading)
- %SYSTEM32%\qwinsta.exe (Sideloading)
- %SYSTEM32%\redircmp.exe (Sideloading)
- %SYSTEM32%\redirusr.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\rendom.exe (Sideloading)
- %SYSTEM32%\repadmin.exe (Sideloading)
- %SYSTEM32%\reset.exe (Sideloading)
- %SYSTEM32%\rwinsta.exe (Sideloading)
- %SYSTEM32%\setspn.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tscon.exe (Sideloading)
- %SYSTEM32%\tskill.exe (Sideloading)
- %SYSTEM32%\w32tm.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
