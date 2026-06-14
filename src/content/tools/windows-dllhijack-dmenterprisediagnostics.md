---
trust_level: community
id: windows-dllhijack-dmenterprisediagnostics
namespace: windows:dllhijack:dmenterprisediagnostics
name: dmenterprisediagnostics.dll
description: "dmenterprisediagnostics.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmenterprisediagnostics.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmenterprisediagnostics.html"
---
examples:
  - description: "Place malicious dmenterprisediagnostics.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmenterprisediagnostics.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\deviceenroller.exe\""

# dmenterprisediagnostics.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)

**Acknowledgement:** Wietze
