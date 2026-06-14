---
trust_level: community
id: windows-dllhijack-srpapi
namespace: windows:dllhijack:srpapi
name: srpapi.dll
description: "srpapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "srpapi.dll"
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
    url: "https://hijacklibs.net/entries/srpapi.html"
---
examples:
  - description: "Place malicious srpapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\srpapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appidpolicyconverter.exe\""

# srpapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appidpolicyconverter.exe (Sideloading)
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
