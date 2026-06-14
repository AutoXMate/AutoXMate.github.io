---
trust_level: community
id: windows-dllhijack-mbaexmlparser
namespace: windows:dllhijack:mbaexmlparser
name: mbaexmlparser.dll
description: "mbaexmlparser.dll — Sideloading hijacking (Microsoft)"
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
  template: "mbaexmlparser.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mbaexmlparser.html"
---
examples:
  - description: "Place malicious mbaexmlparser.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mbaexmlparser.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mbaeparsertask.exe\""

# mbaexmlparser.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mbaeparsertask.exe (Sideloading)

**Acknowledgement:** Chris Spehn
