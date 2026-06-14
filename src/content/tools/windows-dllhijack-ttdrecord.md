---
trust_level: community
id: windows-dllhijack-ttdrecord
namespace: windows:dllhijack:ttdrecord
name: ttdrecord.dll
description: "ttdrecord.dll — Sideloading hijacking (Microsoft)"
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
  template: "ttdrecord.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ttdrecord.html"
---
examples:
  - description: "Place malicious ttdrecord.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ttdrecord.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\tttracer.exe\""

# ttdrecord.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\tttracer.exe (Sideloading)

**Acknowledgement:** Wietze
