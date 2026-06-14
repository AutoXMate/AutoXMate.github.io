---
trust_level: community
id: windows-dllhijack-dsparse
namespace: windows:dllhijack:dsparse
name: dsparse.dll
description: "dsparse.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "dsparse.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dsparse.html"
---
examples:
  - description: "Place malicious dsparse.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dsparse.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dcdiag.exe\""

# dsparse.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\dmcertinst.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\rendom.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
