---
trust_level: community
id: windows-dllhijack-regapi
namespace: windows:dllhijack:regapi
name: regapi.dll
description: "regapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "regapi.dll"
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
    url: "https://hijacklibs.net/entries/regapi.html"
---
examples:
  - description: "Place malicious regapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\regapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\change.exe\""

# regapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\change.exe (Sideloading)
- %SYSTEM32%\chglogon.exe (Sideloading)
- %SYSTEM32%\query.exe (Sideloading)
- %SYSTEM32%\reset.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
