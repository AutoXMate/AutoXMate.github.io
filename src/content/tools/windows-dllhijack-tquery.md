---
trust_level: community
id: windows-dllhijack-tquery
namespace: windows:dllhijack:tquery
name: tquery.dll
description: "tquery.dll — Sideloading hijacking (Microsoft)"
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
  template: "tquery.dll"
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
    url: "https://hijacklibs.net/entries/tquery.html"
---
examples:
  - description: "Place malicious tquery.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tquery.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\searchfilterhost.exe\""

# tquery.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\searchfilterhost.exe (Sideloading)
- %SYSTEM32%\searchprotocolhost.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
