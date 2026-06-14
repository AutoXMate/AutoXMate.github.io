---
trust_level: community
id: windows-dllhijack-ifmon
namespace: windows:dllhijack:ifmon
name: ifmon.dll
description: "ifmon.dll — Sideloading hijacking (Microsoft)"
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
  template: "ifmon.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ifmon.html"
---
examples:
  - description: "Place malicious ifmon.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ifmon.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# ifmon.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
