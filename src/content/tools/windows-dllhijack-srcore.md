---
trust_level: community
id: windows-dllhijack-srcore
namespace: windows:dllhijack:srcore
name: srcore.dll
description: "srcore.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "srcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/srcore.html"
---
examples:
  - description: "Place malicious srcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\srcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rstrui.exe\""

# srcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rstrui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\srtasks.exe (Sideloading)

**Acknowledgement:** Wietze
