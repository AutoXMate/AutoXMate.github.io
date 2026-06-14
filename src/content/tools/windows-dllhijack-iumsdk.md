---
trust_level: community
id: windows-dllhijack-iumsdk
namespace: windows:dllhijack:iumsdk
name: iumsdk.dll
description: "iumsdk.dll — Sideloading hijacking (Microsoft)"
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
  template: "iumsdk.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iumsdk.html"
---
examples:
  - description: "Place malicious iumsdk.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iumsdk.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bioiso.exe\""

# iumsdk.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bioiso.exe (Sideloading)
- %SYSTEM32%\fsiso.exe (Sideloading)
- %SYSTEM32%\ngciso.exe (Sideloading)

**Acknowledgement:** Chris Spehn
