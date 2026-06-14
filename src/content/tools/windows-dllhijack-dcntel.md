---
trust_level: community
id: windows-dllhijack-dcntel
namespace: windows:dllhijack:dcntel
name: dcntel.dll
description: "dcntel.dll — Sideloading hijacking (Microsoft)"
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
  template: "dcntel.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dcntel.html"
---
examples:
  - description: "Place malicious dcntel.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dcntel.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicecensus.exe\""

# dcntel.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicecensus.exe (Sideloading)

**Acknowledgement:** Wietze
