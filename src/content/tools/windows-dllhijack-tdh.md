---
trust_level: community
id: windows-dllhijack-tdh
namespace: windows:dllhijack:tdh
name: tdh.dll
description: "tdh.dll — Sideloading hijacking (Microsoft)"
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
  template: "tdh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tdh.html"
---
examples:
  - description: "Place malicious tdh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tdh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\plasrv.exe\""

# tdh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\plasrv.exe (Sideloading)

**Acknowledgement:** Wietze
