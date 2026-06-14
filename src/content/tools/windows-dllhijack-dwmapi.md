---
trust_level: community
id: windows-dllhijack-dwmapi
namespace: windows:dllhijack:dwmapi
name: dwmapi.dll
description: "dwmapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "dwmapi.dll"
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
    url: "https://hijacklibs.net/entries/dwmapi.html"
---
examples:
  - description: "Place malicious dwmapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dwmapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# dwmapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\devicepairingwizard.exe (Sideloading)
- %SYSTEM32%\displayswitch.exe (Sideloading)
- %SYSTEM32%\dxpserver.exe (Sideloading)
- %SYSTEM32%\fsquirt.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\lockscreencontentserver.exe (Sideloading)
- %SYSTEM32%\mblctr.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\proximityuxhost.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\rdpshell.exe (Sideloading)
- %SYSTEM32%\rdvghelper.exe (Sideloading)
- %SYSTEM32%\sndvol.exe (Sideloading)
- %SYSTEM32%\snippingtool.exe (Sideloading)
- %SYSTEM32%\wmpdmc.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
