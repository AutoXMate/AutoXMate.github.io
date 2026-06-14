---
trust_level: community
id: windows-dllhijack-resutils
namespace: windows:dllhijack:resutils
name: resutils.dll
description: "resutils.dll — Sideloading hijacking (Microsoft)"
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
  template: "resutils.dll"
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
    url: "https://hijacklibs.net/entries/resutils.html"
---
examples:
  - description: "Place malicious resutils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\resutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dfsdiag.exe\""

# resutils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dfsdiag.exe (Sideloading)
- %SYSTEM32%\msdtc.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
