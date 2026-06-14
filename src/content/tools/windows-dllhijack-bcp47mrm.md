---
trust_level: community
id: windows-dllhijack-bcp47mrm
namespace: windows:dllhijack:bcp47mrm
name: bcp47mrm.dll
description: "bcp47mrm.dll — Sideloading hijacking (Microsoft)"
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
  template: "bcp47mrm.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bcp47mrm.html"
---
examples:
  - description: "Place malicious bcp47mrm.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bcp47mrm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mcbuilder.exe\""

# bcp47mrm.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mcbuilder.exe (Sideloading)

**Acknowledgement:** Wietze
