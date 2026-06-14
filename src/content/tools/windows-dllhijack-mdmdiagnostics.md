---
trust_level: community
id: windows-dllhijack-mdmdiagnostics
namespace: windows:dllhijack:mdmdiagnostics
name: mdmdiagnostics.dll
description: "mdmdiagnostics.dll — Sideloading hijacking (Microsoft)"
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
  template: "mdmdiagnostics.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mdmdiagnostics.html"
---
examples:
  - description: "Place malicious mdmdiagnostics.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mdmdiagnostics.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mdmdiagnosticstool.exe\""

# mdmdiagnostics.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)

**Acknowledgement:** Wietze
