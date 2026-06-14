---
trust_level: community
id: windows-dllhijack-radcui
namespace: windows:dllhijack:radcui
name: radcui.dll
description: "radcui.dll — Sideloading hijacking (Microsoft)"
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
  template: "radcui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/radcui.html"
---
examples:
  - description: "Place malicious radcui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\radcui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wkspbroker.exe\""

# radcui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wkspbroker.exe (Sideloading)

**Acknowledgement:** Wietze
