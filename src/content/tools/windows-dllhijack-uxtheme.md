---
trust_level: community
id: windows-dllhijack-uxtheme
namespace: windows:dllhijack:uxtheme
name: uxtheme.dll
description: "uxtheme.dll — Sideloading, Search Order hijacking (Microsoft)"
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
  template: "uxtheme.dll"
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
  - label: "Reference"
    url: "https://skr1x.github.io/keepass-dll-hijacking/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uxtheme.html"
---
examples:
  - description: "Place malicious uxtheme.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\uxtheme.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\atbroker.exe\""

# uxtheme.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\atbroker.exe (Sideloading)
- %SYSTEM32%\cloudnotifications.exe (Sideloading)
- %SYSTEM32%\cttune.exe (Sideloading)
- %SYSTEM32%\displayswitch.exe (Sideloading)
- %SYSTEM32%\ehstorauthn.exe (Sideloading)
- %SYSTEM32%\filehistory.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\isoburn.exe (Sideloading)
- %SYSTEM32%\mblctr.exe (Sideloading)
- %SYSTEM32%\mmc.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\musnotifyicon.exe (Sideloading)
- %SYSTEM32%\passwordonwakesettingflyout.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\sethc.exe (Sideloading)
- %SYSTEM32%\sndvol.exe (Sideloading)
- %SYSTEM32%\snippingtool.exe (Sideloading)
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wfs.exe (Sideloading)
- %SYSTEM32%\wiaacmgr.exe (Sideloading)
- %SYSTEM32%\wiawow64.exe (Sideloading)
- %SYSTEM32%\wmpdmc.exe (Sideloading)
- %PROGRAMFILES%\KeePass Password Safe 2\KeePass.exe (Search Order)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Skrix
