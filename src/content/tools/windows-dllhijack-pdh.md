---
trust_level: community
id: windows-dllhijack-pdh
namespace: windows:dllhijack:pdh
name: pdh.dll
description: "pdh.dll — Sideloading, Environment Variable hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "pdh.dll"
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
    url: "https://hijacklibs.net/entries/pdh.html"
---
examples:
  - description: "Place malicious pdh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\pdh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\plasrv.exe\""

# pdh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\plasrv.exe (Sideloading)
- %SYSTEM32%\relog.exe (Sideloading)
- %SYSTEM32%\taskmgr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tracerpt.exe (Sideloading)
- %SYSTEM32%\typeperf.exe (Sideloading)
- %SYSTEM32%\logman.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
