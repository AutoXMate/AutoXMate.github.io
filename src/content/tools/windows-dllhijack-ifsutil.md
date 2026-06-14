---
trust_level: community
id: windows-dllhijack-ifsutil
namespace: windows:dllhijack:ifsutil
name: ifsutil.dll
description: "ifsutil.dll — Sideloading hijacking (Microsoft)"
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
  template: "ifsutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ifsutil.html"
---
examples:
  - description: "Place malicious ifsutil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ifsutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\convert.exe\""

# ifsutil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\convert.exe (Sideloading)
- %SYSTEM32%\fsavailux.exe (Sideloading)
- %SYSTEM32%\label.exe (Sideloading)
- %SYSTEM32%\recover.exe (Sideloading)
- %SYSTEM32%\xcopy.exe (Sideloading)

**Acknowledgement:** Chris Spehn
