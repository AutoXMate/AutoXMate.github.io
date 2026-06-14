---
trust_level: community
id: windows-dllhijack-clipc
namespace: windows:dllhijack:clipc
name: clipc.dll
description: "clipc.dll — Sideloading hijacking (Microsoft)"
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
  template: "clipc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/clipc.html"
---
examples:
  - description: "Place malicious clipc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\clipc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\licensingdiag.exe\""

# clipc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\licensingdiag.exe (Sideloading)

**Acknowledgement:** Wietze
