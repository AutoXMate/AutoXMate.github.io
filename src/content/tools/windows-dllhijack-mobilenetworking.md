---
trust_level: community
id: windows-dllhijack-mobilenetworking
namespace: windows:dllhijack:mobilenetworking
name: mobilenetworking.dll
description: "mobilenetworking.dll — Sideloading hijacking (Microsoft)"
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
  template: "mobilenetworking.dll"
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
    url: "https://hijacklibs.net/entries/mobilenetworking.html"
---
examples:
  - description: "Place malicious mobilenetworking.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mobilenetworking.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mbaeparsertask.exe\""

# mobilenetworking.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mbaeparsertask.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
