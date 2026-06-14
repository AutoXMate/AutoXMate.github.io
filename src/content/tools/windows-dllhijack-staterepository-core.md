---
trust_level: community
id: windows-dllhijack-staterepository-core
namespace: windows:dllhijack:staterepository-core
name: staterepository.core.dll
description: "staterepository.core.dll — Sideloading hijacking (Microsoft)"
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
  template: "staterepository.core.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/staterepository-core.html"
---
examples:
  - description: "Place malicious staterepository.core.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\staterepository.core.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\applytrustoffline.exe\""

# staterepository.core.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\applytrustoffline.exe (Sideloading)
- %SYSTEM32%\lpremove.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
