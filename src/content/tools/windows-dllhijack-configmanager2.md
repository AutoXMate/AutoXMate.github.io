---
trust_level: community
id: windows-dllhijack-configmanager2
namespace: windows:dllhijack:configmanager2
name: configmanager2.dll
description: "configmanager2.dll — Sideloading hijacking (Microsoft)"
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
  template: "configmanager2.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/configmanager2.html"
---
examples:
  - description: "Place malicious configmanager2.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\configmanager2.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\hvsievaluator.exe\""

# configmanager2.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\hvsievaluator.exe (Sideloading)

**Acknowledgement:** Chris Spehn
