---
trust_level: community
id: windows-dllhijack-iumbase
namespace: windows:dllhijack:iumbase
name: iumbase.dll
description: "iumbase.dll — Sideloading hijacking (Microsoft)"
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
  template: "iumbase.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iumbase.html"
---
examples:
  - description: "Place malicious iumbase.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iumbase.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bioiso.exe\""

# iumbase.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bioiso.exe (Sideloading)
- %SYSTEM32%\fsiso.exe (Sideloading)
- %SYSTEM32%\ngciso.exe (Sideloading)

**Acknowledgement:** Wietze
