---
trust_level: community
id: windows-dllhijack-windows-ui-immersive
namespace: windows:dllhijack:windows-ui-immersive
name: windows.ui.immersive.dll
description: "windows.ui.immersive.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "windows.ui.immersive.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windows-ui-immersive.html"
---
examples:
  - description: "Place malicious windows.ui.immersive.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windows.ui.immersive.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dmnotificationbroker.exe\""

# windows.ui.immersive.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dmnotificationbroker.exe (Sideloading)
- %SYSTEM32%\phoneactivate.exe (Sideloading)

**Acknowledgement:** Chris Spehn
