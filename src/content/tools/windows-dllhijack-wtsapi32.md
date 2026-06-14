---
trust_level: community
id: windows-dllhijack-wtsapi32
namespace: windows:dllhijack:wtsapi32
name: wtsapi32.dll
description: "wtsapi32.dll — Sideloading hijacking (Microsoft)"
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
  template: "wtsapi32.dll"
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
    url: "https://hijacklibs.net/entries/wtsapi32.html"
---
examples:
  - description: "Place malicious wtsapi32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wtsapi32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appvclient.exe\""

# wtsapi32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appvclient.exe (Sideloading)
- %SYSTEM32%\bdeuisrv.exe (Sideloading)
- %SYSTEM32%\customshellhost.exe (Sideloading)
- %SYSTEM32%\magnify.exe (Sideloading)
- %SYSTEM32%\mblctr.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\raserver.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\rdpinput.exe (Sideloading)
- %SYSTEM32%\rdpinit.exe (Sideloading)
- %SYSTEM32%\rdpshell.exe (Sideloading)
- %SYSTEM32%\rdvghelper.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- %SYSTEM32%\sethc.exe (Sideloading)
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wusa.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Austin Worline
