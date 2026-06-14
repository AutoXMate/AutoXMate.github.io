---
trust_level: community
id: windows-dllhijack-mi
namespace: windows:dllhijack:mi
name: mi.dll
description: "mi.dll — Sideloading hijacking (Microsoft)"
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
  template: "mi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/39828/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mi.html"
---
examples:
  - description: "Place malicious mi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\winrs.exe\""

# mi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\winrs.exe (Sideloading)
- %SYSTEM32%\wsmanhttpconfig.exe (Sideloading)
- %SYSTEM32%\wsmprovhost.exe (Sideloading)

**Acknowledgement:** Wietze
