---
trust_level: community
id: windows-dllhijack-opcservices
namespace: windows:dllhijack:opcservices
name: opcservices.dll
description: opcservices.dll — Sideloading hijacking (Microsoft)
author: Chris Spehn
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: opcservices.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/opcservices.html
features:
- process-manip
---

examples:
  - description: "Place malicious opcservices.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\opcservices.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\proximityuxhost.exe\""

# opcservices.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\proximityuxhost.exe (Sideloading)

**Acknowledgement:** Chris Spehn
