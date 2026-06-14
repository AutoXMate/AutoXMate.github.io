---
trust_level: community
id: windows-dllhijack-dmpushproxy
namespace: windows:dllhijack:dmpushproxy
name: dmpushproxy.dll
description: "dmpushproxy.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmpushproxy.dll"
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
    url: "https://hijacklibs.net/entries/dmpushproxy.html"
---
examples:
  - description: "Place malicious dmpushproxy.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmpushproxy.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dmcfghost.exe\""

# dmpushproxy.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dmcfghost.exe (Sideloading)
- %SYSTEM32%\omadmrpc.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
