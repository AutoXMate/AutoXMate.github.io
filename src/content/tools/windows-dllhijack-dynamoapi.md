---
trust_level: community
id: windows-dllhijack-dynamoapi
namespace: windows:dllhijack:dynamoapi
name: dynamoapi.dll
description: "dynamoapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "dynamoapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dynamoapi.html"
---
examples:
  - description: "Place malicious dynamoapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dynamoapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mdmdiagnosticstool.exe\""

# dynamoapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)

**Acknowledgement:** Wietze
