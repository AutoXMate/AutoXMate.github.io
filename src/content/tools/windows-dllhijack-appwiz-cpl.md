---
trust_level: community
id: windows-dllhijack-appwiz-cpl
namespace: windows:dllhijack:appwiz-cpl
name: appwiz.cpl.dll
description: "appwiz.cpl.dll — Sideloading hijacking (Microsoft)"
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
  template: "appwiz.cpl.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2024/01/06/1-little-known-secret-of-fondue-exe/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/appwiz-cpl.html"
---
examples:
  - description: "Place malicious appwiz.cpl.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\appwiz.cpl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fondue.exe\""

# appwiz.cpl.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fondue.exe (Sideloading)

**Acknowledgement:** Adam
