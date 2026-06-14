---
trust_level: community
id: windows-dllhijack-drvstore
namespace: windows:dllhijack:drvstore
name: drvstore.dll
description: "drvstore.dll — Sideloading hijacking (Microsoft)"
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
  template: "drvstore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "Reference"
    url: "https://www.microsoft.com/en-us/download/details.aspx?id=105437"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/drvstore.html"
---
examples:
  - description: "Place malicious drvstore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\drvstore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\infdefaultinstall.exe\""

# drvstore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\infdefaultinstall.exe (Sideloading)
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- hvciscan_amd64.exe (Sideloading)

**Acknowledgement:** Chris Spehn
