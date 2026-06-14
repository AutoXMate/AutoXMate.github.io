---
trust_level: community
id: windows-dllhijack-osksupport
namespace: windows:dllhijack:osksupport
name: osksupport.dll
description: "osksupport.dll — Sideloading hijacking (Microsoft)"
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
  template: "osksupport.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/osksupport.html"
---
examples:
  - description: "Place malicious osksupport.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\osksupport.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\osk.exe\""

# osksupport.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\osk.exe (Sideloading)

**Acknowledgement:** Wietze
