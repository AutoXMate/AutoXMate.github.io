---
trust_level: community
id: windows-dllhijack-wecapi
namespace: windows:dllhijack:wecapi
name: wecapi.dll
description: "wecapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "wecapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wecapi.html"
---
examples:
  - description: "Place malicious wecapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wecapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wecutil.exe\""

# wecapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wecutil.exe (Sideloading)

**Acknowledgement:** Wietze
