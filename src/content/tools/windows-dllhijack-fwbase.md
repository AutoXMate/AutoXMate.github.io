---
trust_level: community
id: windows-dllhijack-fwbase
namespace: windows:dllhijack:fwbase
name: fwbase.dll
description: "fwbase.dll — Sideloading hijacking (Microsoft)"
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
  template: "fwbase.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fwbase.html"
---
examples:
  - description: "Place malicious fwbase.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fwbase.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\checknetisolation.exe\""

# fwbase.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\checknetisolation.exe (Sideloading)
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\lpremove.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
