---
trust_level: community
id: windows-dllhijack-srmtrace
namespace: windows:dllhijack:srmtrace
name: srmtrace.dll
description: "srmtrace.dll — Sideloading hijacking (Microsoft)"
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
  template: "srmtrace.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/srmtrace.html"
---
examples:
  - description: "Place malicious srmtrace.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\srmtrace.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dirquota.exe\""

# srmtrace.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dirquota.exe (Sideloading)
- %SYSTEM32%\filescrn.exe (Sideloading)
- %SYSTEM32%\storrept.exe (Sideloading)

**Acknowledgement:** Chris Spehn
