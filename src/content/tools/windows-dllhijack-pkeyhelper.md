---
trust_level: community
id: windows-dllhijack-pkeyhelper
namespace: windows:dllhijack:pkeyhelper
name: pkeyhelper.dll
description: "pkeyhelper.dll — Sideloading hijacking (Microsoft)"
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
  template: "pkeyhelper.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/pkeyhelper.html"
---
examples:
  - description: "Place malicious pkeyhelper.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\pkeyhelper.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\sppsvc.exe\""

# pkeyhelper.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\sppsvc.exe (Sideloading)

**Acknowledgement:** Chris Spehn
