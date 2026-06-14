---
trust_level: community
id: windows-dllhijack-d2d1
namespace: windows:dllhijack:d2d1
name: d2d1.dll
description: "d2d1.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "d2d1.dll"
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
    url: "https://hijacklibs.net/entries/d2d1.html"
---
examples:
  - description: "Place malicious d2d1.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d2d1.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dataexchangehost.exe\""

# d2d1.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dataexchangehost.exe (Sideloading)
- %SYSTEM32%\dwm.exe (Sideloading)
- %SYSTEM32%\eoaexperiences.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\vsgraphicsdesktopengine.exe (Sideloading)
- %SYSTEM32%\vsgraphicsremoteengine.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
