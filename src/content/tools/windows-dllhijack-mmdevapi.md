---
trust_level: community
id: windows-dllhijack-mmdevapi
namespace: windows:dllhijack:mmdevapi
name: mmdevapi.dll
description: "mmdevapi.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "mmdevapi.dll"
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
    url: "https://hijacklibs.net/entries/mmdevapi.html"
---
examples:
  - description: "Place malicious mmdevapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mmdevapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\audiodg.exe\""

# mmdevapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\audiodg.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\devicecensus.exe (Environment Variable)
- %SYSTEM32%\mblctr.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\presentationsettings.exe (Environment Variable)
- %SYSTEM32%\sndvol.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
