---
trust_level: community
id: windows-dllhijack-urlmon
namespace: windows:dllhijack:urlmon
name: urlmon.dll
description: "urlmon.dll — Sideloading hijacking (Microsoft)"
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
  template: "urlmon.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/urlmon.html"
---
examples:
  - description: "Place malicious urlmon.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\urlmon.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bytecodegenerator.exe\""

# urlmon.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bytecodegenerator.exe (Sideloading)
- %SYSTEM32%\ie4uinit.exe (Sideloading)
- %SYSTEM32%\ldifde.exe (Sideloading)
- %SYSTEM32%\presentationhost.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Chris Spehn
