---
trust_level: community
id: windows-dllhijack-sas
namespace: windows:dllhijack:sas
name: sas.dll
description: "sas.dll — Sideloading hijacking (Microsoft)"
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
  template: "sas.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sas.html"
---
examples:
  - description: "Place malicious sas.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sas.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\quickassist.exe\""

# sas.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\quickassist.exe (Sideloading)

**Acknowledgement:** Wietze
