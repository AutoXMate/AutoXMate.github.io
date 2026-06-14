---
trust_level: community
id: windows-dllhijack-iedkcs32
namespace: windows:dllhijack:iedkcs32
name: iedkcs32.dll
description: "iedkcs32.dll — Sideloading hijacking (Microsoft)"
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
  template: "iedkcs32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iedkcs32.html"
---
examples:
  - description: "Place malicious iedkcs32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iedkcs32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ie4uinit.exe\""

# iedkcs32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ie4uinit.exe (Sideloading)

**Acknowledgement:** Wietze
