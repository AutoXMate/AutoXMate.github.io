---
trust_level: community
id: windows-dllhijack-winsync
namespace: windows:dllhijack:winsync
name: winsync.dll
description: "winsync.dll — Sideloading hijacking (Microsoft)"
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
  template: "winsync.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/winsync.html"
---
examples:
  - description: "Place malicious winsync.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winsync.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\synchost.exe\""

# winsync.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\synchost.exe (Sideloading)

**Acknowledgement:** Chris Spehn
