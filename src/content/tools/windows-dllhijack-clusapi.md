---
trust_level: community
id: windows-dllhijack-clusapi
namespace: windows:dllhijack:clusapi
name: clusapi.dll
description: "clusapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "clusapi.dll"
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
    url: "https://hijacklibs.net/entries/clusapi.html"
---
examples:
  - description: "Place malicious clusapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\clusapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dfsrdiag.exe\""

# clusapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\msdtc.exe (Sideloading)
- %SYSTEM32%\tieringengineservice.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
