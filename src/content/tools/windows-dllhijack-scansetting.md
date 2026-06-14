---
trust_level: community
id: windows-dllhijack-scansetting
namespace: windows:dllhijack:scansetting
name: scansetting.dll
description: "scansetting.dll — Sideloading hijacking (Microsoft)"
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
  template: "scansetting.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/scansetting.html"
---
examples:
  - description: "Place malicious scansetting.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\scansetting.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wiaacmgr.exe\""

# scansetting.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wiaacmgr.exe (Sideloading)
- %SYSTEM32%\wiawow64.exe (Sideloading)

**Acknowledgement:** Wietze
