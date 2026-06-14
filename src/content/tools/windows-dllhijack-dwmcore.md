---
trust_level: community
id: windows-dllhijack-dwmcore
namespace: windows:dllhijack:dwmcore
name: dwmcore.dll
description: "dwmcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "dwmcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dwmcore.html"
---
examples:
  - description: "Place malicious dwmcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dwmcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dwm.exe\""

# dwmcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dwm.exe (Sideloading)

**Acknowledgement:** Wietze
