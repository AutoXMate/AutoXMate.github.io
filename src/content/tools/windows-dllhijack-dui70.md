---
trust_level: community
id: windows-dllhijack-dui70
namespace: windows:dllhijack:dui70
name: dui70.dll
description: "dui70.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "dui70.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dui70.html"
---
examples:
  - description: "Place malicious dui70.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dui70.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bdeunlock.exe\""

# dui70.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bdeunlock.exe (Sideloading)
- %SYSTEM32%\camerasettings.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\dmnotificationbroker.exe (Sideloading)
- %SYSTEM32%\dpapimig.exe (Sideloading)
- %SYSTEM32%\licensingui.exe (Sideloading)
- %SYSTEM32%\optionalfeatures.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\passwordonwakesettingflyout.exe (Sideloading)
- %SYSTEM32%\phoneactivate.exe (Sideloading)
- %SYSTEM32%\proximityuxhost.exe (Sideloading)
- %SYSTEM32%\rasphone.exe (Environment Variable)
- %SYSTEM32%\sessionmsg.exe (Sideloading)
- %SYSTEM32%\sethc.exe (Sideloading)
- %SYSTEM32%\sysreseterr.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading)
- %SYSTEM32%\systemsettingsremovedevice.exe (Sideloading)
- %SYSTEM32%\utilman.exe (Sideloading)
- %SYSTEM32%\windowsactiondialog.exe (Sideloading)
- %SYSTEM32%\wlrmdr.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
