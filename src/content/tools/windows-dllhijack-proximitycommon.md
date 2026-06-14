---
trust_level: community
id: windows-dllhijack-proximitycommon
namespace: windows:dllhijack:proximitycommon
name: proximitycommon.dll
description: "proximitycommon.dll — Sideloading hijacking (Microsoft)"
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
  template: "proximitycommon.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/proximitycommon.html"
---
examples:
  - description: "Place malicious proximitycommon.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\proximitycommon.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\proximityuxhost.exe\""

# proximitycommon.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\proximityuxhost.exe (Sideloading)

**Acknowledgement:** Chris Spehn
