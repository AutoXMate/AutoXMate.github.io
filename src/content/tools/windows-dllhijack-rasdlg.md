---
trust_level: community
id: windows-dllhijack-rasdlg
namespace: windows:dllhijack:rasdlg
name: rasdlg.dll
description: "rasdlg.dll — Sideloading hijacking (Microsoft)"
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
  template: "rasdlg.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rasdlg.html"
---
examples:
  - description: "Place malicious rasdlg.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\rasdlg.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rasautou.exe\""

# rasdlg.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rasautou.exe (Sideloading)

**Acknowledgement:** Chris Spehn
