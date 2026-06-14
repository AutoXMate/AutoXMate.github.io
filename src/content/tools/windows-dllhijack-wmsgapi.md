---
trust_level: community
id: windows-dllhijack-wmsgapi
namespace: windows:dllhijack:wmsgapi
name: wmsgapi.dll
description: "wmsgapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "wmsgapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wmsgapi.html"
---
examples:
  - description: "Place malicious wmsgapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wmsgapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\osk.exe\""

# wmsgapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\osk.exe (Sideloading)

**Acknowledgement:** Wietze
