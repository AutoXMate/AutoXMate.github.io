---
trust_level: community
id: windows-dllhijack-osbaseln
namespace: windows:dllhijack:osbaseln
name: osbaseln.dll
description: "osbaseln.dll — Sideloading hijacking (Microsoft)"
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
  template: "osbaseln.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/osbaseln.html"
---
examples:
  - description: "Place malicious osbaseln.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\osbaseln.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fondue.exe\""

# osbaseln.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fondue.exe (Sideloading)
- %SYSTEM32%\optionalfeatures.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
