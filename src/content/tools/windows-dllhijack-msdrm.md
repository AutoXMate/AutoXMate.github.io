---
trust_level: community
id: windows-dllhijack-msdrm
namespace: windows:dllhijack:msdrm
name: msdrm.dll
description: "msdrm.dll — Sideloading hijacking (Microsoft)"
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
  template: "msdrm.dll"
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
    url: "https://hijacklibs.net/entries/msdrm.html"
---
examples:
  - description: "Place malicious msdrm.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msdrm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\gamepanel.exe\""

# msdrm.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\rmactivate.exe (Sideloading)
- %SYSTEM32%\rmactivate_isv.exe (Sideloading)
- %SYSTEM32%\snippingtool.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
