---
trust_level: community
id: windows-dllhijack-getuname
namespace: windows:dllhijack:getuname
name: getuname.dll
description: "getuname.dll — Sideloading hijacking (Microsoft)"
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
  template: "getuname.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/getuname.html"
---
examples:
  - description: "Place malicious getuname.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\getuname.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\charmap.exe\""

# getuname.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\charmap.exe (Sideloading)

**Acknowledgement:** Wietze
