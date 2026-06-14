---
trust_level: community
id: windows-dllhijack-uireng
namespace: windows:dllhijack:uireng
name: uireng.dll
description: "uireng.dll — Sideloading hijacking (Microsoft)"
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
  template: "uireng.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uireng.html"
---
examples:
  - description: "Place malicious uireng.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\uireng.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\psr.exe\""

# uireng.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\psr.exe (Sideloading)

**Acknowledgement:** Wietze
