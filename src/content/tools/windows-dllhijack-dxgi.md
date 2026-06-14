---
trust_level: community
id: windows-dllhijack-dxgi
namespace: windows:dllhijack:dxgi
name: dxgi.dll
description: "dxgi.dll — Sideloading hijacking (Microsoft)"
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
  template: "dxgi.dll"
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
    url: "https://hijacklibs.net/entries/dxgi.html"
---
examples:
  - description: "Place malicious dxgi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dxgi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\applicationframehost.exe\""

# dxgi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\applicationframehost.exe (Sideloading)
- %SYSTEM32%\dataexchangehost.exe (Sideloading)
- %SYSTEM32%\dwm.exe (Sideloading)
- %SYSTEM32%\dxgiadaptercache.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\mdeserver.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\vsgraphicsremoteengine.exe (Sideloading)
- %SYSTEM32%\winsat.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
