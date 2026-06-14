---
trust_level: community
id: windows-dllhijack-appxalluserstore
namespace: windows:dllhijack:appxalluserstore
name: appxalluserstore.dll
description: "appxalluserstore.dll — Sideloading hijacking (Microsoft)"
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
  template: "appxalluserstore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/appxalluserstore.html"
---
examples:
  - description: "Place malicious appxalluserstore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\appxalluserstore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\lpremove.exe\""

# appxalluserstore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\lpremove.exe (Sideloading)

**Acknowledgement:** Wietze
