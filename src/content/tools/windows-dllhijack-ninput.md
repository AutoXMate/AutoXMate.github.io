---
trust_level: community
id: windows-dllhijack-ninput
namespace: windows:dllhijack:ninput
name: ninput.dll
description: ninput.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
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
  template: ninput.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/ninput.html
features:
- requires-root
---

examples:
  - description: "Place malicious ninput.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ninput.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\multidigimon.exe\""

# ninput.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\multidigimon.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tabcal.exe (Sideloading)

**Acknowledgement:** Wietze
