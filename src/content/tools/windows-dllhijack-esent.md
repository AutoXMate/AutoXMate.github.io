---
trust_level: community
id: windows-dllhijack-esent
namespace: windows:dllhijack:esent
name: esent.dll
description: "esent.dll — Sideloading hijacking (Microsoft)"
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
  template: "esent.dll"
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
    url: "https://hijacklibs.net/entries/esent.html"
---
examples:
  - description: "Place malicious esent.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\esent.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dfsrdiag.exe\""

# esent.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\dsdbutil.exe (Sideloading)
- %SYSTEM32%\esentutl.exe (Sideloading)
- %SYSTEM32%\tieringengineservice.exe (Sideloading)
- %SYSTEM32%\ntdsutil.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
