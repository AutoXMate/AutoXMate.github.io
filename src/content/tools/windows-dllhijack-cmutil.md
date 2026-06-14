---
trust_level: community
id: windows-dllhijack-cmutil
namespace: windows:dllhijack:cmutil
name: cmutil.dll
description: "cmutil.dll — Sideloading hijacking (Microsoft)"
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
  template: "cmutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cmutil.html"
---
examples:
  - description: "Place malicious cmutil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cmutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cmstp.exe\""

# cmutil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cmstp.exe (Sideloading)

**Acknowledgement:** Chris Spehn
