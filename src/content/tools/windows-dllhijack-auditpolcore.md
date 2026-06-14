---
trust_level: community
id: windows-dllhijack-auditpolcore
namespace: windows:dllhijack:auditpolcore
name: auditpolcore.dll
description: "auditpolcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "auditpolcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/auditpolcore.html"
---
examples:
  - description: "Place malicious auditpolcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\auditpolcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\auditpol.exe\""

# auditpolcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\auditpol.exe (Sideloading)

**Acknowledgement:** Wietze
