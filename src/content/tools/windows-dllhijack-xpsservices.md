---
trust_level: community
id: windows-dllhijack-xpsservices
namespace: windows:dllhijack:xpsservices
name: xpsservices.dll
description: "xpsservices.dll — Sideloading hijacking (Microsoft)"
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
  template: "xpsservices.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/xpsservices.html"
---
examples:
  - description: "Place malicious xpsservices.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\xpsservices.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\printfilterpipelinesvc.exe\""

# xpsservices.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\printfilterpipelinesvc.exe (Sideloading)

**Acknowledgement:** Chris Spehn
