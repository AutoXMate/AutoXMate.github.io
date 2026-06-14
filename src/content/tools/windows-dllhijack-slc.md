---
trust_level: community
id: windows-dllhijack-slc
namespace: windows:dllhijack:slc
name: slc.dll
description: "slc.dll — Sideloading hijacking (Microsoft)"
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
  template: "slc.dll"
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
    url: "https://hijacklibs.net/entries/slc.html"
---
examples:
  - description: "Place malicious slc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\slc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msinfo32.exe\""

# slc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msinfo32.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\packageinspector.exe (Sideloading)
- %SYSTEM32%\phoneactivate.exe (Sideloading)
- %SYSTEM32%\slui.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
