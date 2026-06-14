---
trust_level: community
id: windows-dllhijack-wsmsvc
namespace: windows:dllhijack:wsmsvc
name: wsmsvc.dll
description: "wsmsvc.dll — Sideloading hijacking (Microsoft)"
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
  template: "wsmsvc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wsmsvc.html"
---
examples:
  - description: "Place malicious wsmsvc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wsmsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\winrs.exe\""

# wsmsvc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\winrs.exe (Sideloading)
- %SYSTEM32%\wsmanhttpconfig.exe (Sideloading)
- %SYSTEM32%\wsmprovhost.exe (Sideloading)

**Acknowledgement:** Chris Spehn
