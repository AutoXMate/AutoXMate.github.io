---
trust_level: community
id: windows-dllhijack-wmpdui
namespace: windows:dllhijack:wmpdui
name: wmpdui.dll
description: "wmpdui.dll — Sideloading hijacking (Microsoft)"
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
  template: "wmpdui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wmpdui.html"
---
examples:
  - description: "Place malicious wmpdui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wmpdui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wmpdmc.exe\""

# wmpdui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wmpdmc.exe (Sideloading)

**Acknowledgement:** Wietze
