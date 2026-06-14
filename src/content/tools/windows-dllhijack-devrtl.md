---
trust_level: community
id: windows-dllhijack-devrtl
namespace: windows:dllhijack:devrtl
name: devrtl.dll
description: devrtl.dll — Sideloading hijacking (Microsoft)
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
  template: devrtl.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/devrtl.html
features:
- requires-root
---

examples:
  - description: "Place malicious devrtl.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\devrtl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\drvinst.exe\""

# devrtl.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\drvinst.exe (Sideloading)
- %SYSTEM32%\pnpunattend.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wowreg32.exe (Sideloading)

**Acknowledgement:** Wietze
