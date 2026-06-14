---
trust_level: community
id: windows-dllhijack-mtxclu
namespace: windows:dllhijack:mtxclu
name: mtxclu.dll
description: "mtxclu.dll — Sideloading hijacking (Microsoft)"
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
  template: "mtxclu.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mtxclu.html"
---
examples:
  - description: "Place malicious mtxclu.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mtxclu.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msdtc.exe\""

# mtxclu.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msdtc.exe (Sideloading)

**Acknowledgement:** Wietze
