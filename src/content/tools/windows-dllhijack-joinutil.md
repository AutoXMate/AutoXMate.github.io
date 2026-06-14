---
trust_level: community
id: windows-dllhijack-joinutil
namespace: windows:dllhijack:joinutil
name: joinutil.dll
description: "joinutil.dll — Sideloading hijacking (Microsoft)"
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
  template: "joinutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/joinutil.html"
---
examples:
  - description: "Place malicious joinutil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\joinutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\djoin.exe\""

# joinutil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\djoin.exe (Sideloading)

**Acknowledgement:** Wietze
