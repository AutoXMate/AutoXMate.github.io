---
trust_level: community
id: windows-dllhijack-iscsium
namespace: windows:dllhijack:iscsium
name: iscsium.dll
description: iscsium.dll — Sideloading hijacking (Microsoft)
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
  template: iscsium.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/iscsium.html
features:
- requires-root
---

examples:
  - description: "Place malicious iscsium.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iscsium.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\iscsicli.exe\""

# iscsium.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\iscsicli.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
