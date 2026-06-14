---
trust_level: community
id: windows-dllhijack-linkinfo
namespace: windows:dllhijack:linkinfo
name: linkinfo.dll
description: "linkinfo.dll — Sideloading hijacking (Microsoft)"
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
  template: "linkinfo.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/linkinfo.html"
---
examples:
  - description: "Place malicious linkinfo.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\linkinfo.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# linkinfo.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)

**Acknowledgement:** Wietze
