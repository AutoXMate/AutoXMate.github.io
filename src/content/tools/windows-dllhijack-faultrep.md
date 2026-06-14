---
trust_level: community
id: windows-dllhijack-faultrep
namespace: windows:dllhijack:faultrep
name: faultrep.dll
description: "faultrep.dll — Sideloading hijacking (Microsoft)"
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
  template: "faultrep.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/faultrep.html"
---
examples:
  - description: "Place malicious faultrep.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\faultrep.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\werfault.exe\""

# faultrep.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\werfault.exe (Sideloading)
- %SYSTEM32%\werfaultsecure.exe (Sideloading)

**Acknowledgement:** Wietze
