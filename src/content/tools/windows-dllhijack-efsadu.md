---
trust_level: community
id: windows-dllhijack-efsadu
namespace: windows:dllhijack:efsadu
name: efsadu.dll
description: "efsadu.dll — Sideloading hijacking (Microsoft)"
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
  template: "efsadu.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/efsadu.html"
---
examples:
  - description: "Place malicious efsadu.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\efsadu.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\efsui.exe\""

# efsadu.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)

**Acknowledgement:** Wietze
