---
trust_level: community
id: windows-dllhijack-edgeiso
namespace: windows:dllhijack:edgeiso
name: edgeiso.dll
description: "edgeiso.dll — Sideloading hijacking (Microsoft)"
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
  template: "edgeiso.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/edgeiso.html"
---
examples:
  - description: "Place malicious edgeiso.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\edgeiso.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\microsoftedgebchost.exe\""

# edgeiso.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\microsoftedgebchost.exe (Sideloading)
- %SYSTEM32%\microsoftedgecp.exe (Sideloading)
- %SYSTEM32%\microsoftedgedevtools.exe (Sideloading)
- %SYSTEM32%\microsoftedgesh.exe (Sideloading)

**Acknowledgement:** Chris Spehn
