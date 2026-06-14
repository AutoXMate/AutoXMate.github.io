---
trust_level: community
id: windows-dllhijack-mfcore
namespace: windows:dllhijack:mfcore
name: mfcore.dll
description: "mfcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "mfcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mfcore.html"
---
examples:
  - description: "Place malicious mfcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mfcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mfpmp.exe\""

# mfcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mfpmp.exe (Sideloading)

**Acknowledgement:** Wietze
