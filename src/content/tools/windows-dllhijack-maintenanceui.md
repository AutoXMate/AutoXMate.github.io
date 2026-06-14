---
trust_level: community
id: windows-dllhijack-maintenanceui
namespace: windows:dllhijack:maintenanceui
name: maintenanceui.dll
description: maintenanceui.dll — Sideloading hijacking (Microsoft)
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
  template: maintenanceui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/maintenanceui.html
features:
- requires-root
---

examples:
  - description: "Place malicious maintenanceui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\maintenanceui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mschedexe.exe\""

# maintenanceui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mschedexe.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
