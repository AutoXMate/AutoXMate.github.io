---
trust_level: community
id: windows-dllhijack-framedynos
namespace: windows:dllhijack:framedynos
name: framedynos.dll
description: "framedynos.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "framedynos.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/framedynos.html"
---
examples:
  - description: "Place malicious framedynos.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\framedynos.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dfsrdiag.exe\""

# framedynos.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\driverquery.exe (Sideloading)
- %SYSTEM32%\getmac.exe (Sideloading)
- %SYSTEM32%\openfiles.exe (Sideloading)
- %SYSTEM32%\taskkill.exe (Sideloading)

**Acknowledgement:** Chris Spehn
