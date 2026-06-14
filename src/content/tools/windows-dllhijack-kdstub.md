---
trust_level: community
id: windows-dllhijack-kdstub
namespace: windows:dllhijack:kdstub
name: kdstub.dll
description: "kdstub.dll — Sideloading hijacking (Microsoft)"
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
  template: "kdstub.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/kdstub.html"
---
examples:
  - description: "Place malicious kdstub.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\kdstub.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\hvax64.exe\""

# kdstub.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\hvax64.exe (Sideloading)
- %SYSTEM32%\hvix64.exe (Sideloading)

**Acknowledgement:** Wietze
