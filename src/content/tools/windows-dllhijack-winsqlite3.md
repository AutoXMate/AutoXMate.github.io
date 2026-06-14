---
trust_level: community
id: windows-dllhijack-winsqlite3
namespace: windows:dllhijack:winsqlite3
name: winsqlite3.dll
description: "winsqlite3.dll — Sideloading hijacking (Microsoft)"
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
  template: "winsqlite3.dll"
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
    url: "https://hijacklibs.net/entries/winsqlite3.html"
---
examples:
  - description: "Place malicious winsqlite3.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winsqlite3.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\browserexport.exe\""

# winsqlite3.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\browserexport.exe (Sideloading)
- %SYSTEM32%\mousocoreworker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
