---
trust_level: community
id: windows-dllhijack-dusmapi
namespace: windows:dllhijack:dusmapi
name: dusmapi.dll
description: "dusmapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "dusmapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dusmapi.html"
---
examples:
  - description: "Place malicious dusmapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dusmapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\datausagelivetiletask.exe\""

# dusmapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\datausagelivetiletask.exe (Sideloading)

**Acknowledgement:** Wietze
