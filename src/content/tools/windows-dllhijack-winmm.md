---
trust_level: community
id: windows-dllhijack-winmm
namespace: windows:dllhijack:winmm
name: winmm.dll
description: "winmm.dll — Sideloading hijacking (Microsoft)"
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
  template: "winmm.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securelist.com/wastedlocker-technical-analysis/97944/"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "Reference"
    url: "https://ctrlaltintel.com/research/FudCrypt-analysis-1/"
  - label: "Reference"
    url: "https://support.zoom.com/hc/en/article?sysparm_article=KB0064484"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/winmm.html"
---
examples:
  - description: "Place malicious winmm.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winmm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mblctr.exe\""

# winmm.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mblctr.exe (Sideloading)
- %SYSTEM32%\mspaint.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\presentationsettings.exe (Sideloading)
- %SYSTEM32%\proximityuxhost.exe (Sideloading)
- %SYSTEM32%\wfs.exe (Sideloading)
- %SYSTEM32%\winsat.exe (Sideloading) [AutoElevate]
- %APPDATA%\Zoom\bin_%VERSION%\Zoom.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Josh Allman
