---
trust_level: community
id: windows-dllhijack-dxcore
namespace: windows:dllhijack:dxcore
name: dxcore.dll
description: "dxcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "dxcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dxcore.html"
---
examples:
  - description: "Place malicious dxcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dxcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\taskmgr.exe\""

# dxcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\taskmgr.exe (Sideloading)

**Acknowledgement:** Chris Spehn
