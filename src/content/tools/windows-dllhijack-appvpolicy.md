---
trust_level: community
id: windows-dllhijack-appvpolicy
namespace: windows:dllhijack:appvpolicy
name: appvpolicy.dll
description: "appvpolicy.dll — Sideloading hijacking (Microsoft)"
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
  template: "appvpolicy.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/appvpolicy.html"
---
examples:
  - description: "Place malicious appvpolicy.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\appvpolicy.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appvclient.exe\""

# appvpolicy.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appvclient.exe (Sideloading)

**Acknowledgement:** Chris Spehn
