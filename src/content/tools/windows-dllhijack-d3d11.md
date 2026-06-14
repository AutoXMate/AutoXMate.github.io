---
trust_level: community
id: windows-dllhijack-d3d11
namespace: windows:dllhijack:d3d11
name: d3d11.dll
description: d3d11.dll — Sideloading hijacking (Microsoft)
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
  template: d3d11.dll
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
  url: https://blog.amartinsec.com/blog/dllhijacking/
- label: HijackLibs
  url: https://hijacklibs.net/entries/d3d11.html
features:
- requires-root
---

examples:
  - description: "Place malicious d3d11.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d3d11.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dataexchangehost.exe\""

# d3d11.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dataexchangehost.exe (Sideloading)
- %SYSTEM32%\dwm.exe (Sideloading)
- %SYSTEM32%\dxcap.exe (Sideloading)
- %SYSTEM32%\dxgiadaptercache.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\mdeserver.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\vsgraphicsdesktopengine.exe (Sideloading)
- %SYSTEM32%\vsgraphicsremoteengine.exe (Sideloading)
- %SYSTEM32%\winsat.exe (Sideloading) [AutoElevate]
- %PROGRAMFILES%\Steam\steamapps\common\wallpaper_engine\wallpaper32.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Josh Allman
