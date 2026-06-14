---
trust_level: community
id: windows-dllhijack-systemsettingsthresholdadminflowui
namespace: windows:dllhijack:systemsettingsthresholdadminflowui
name: systemsettingsthresholdadminflowui.dll
description: systemsettingsthresholdadminflowui.dll — Sideloading hijacking (Microsoft)
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
  template: systemsettingsthresholdadminflowui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/systemsettingsthresholdadminflowui.html
features:
- requires-root
---

examples:
  - description: "Place malicious systemsettingsthresholdadminflowui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\systemsettingsthresholdadminflowui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\systemsettingsadminflows.exe\""

# systemsettingsthresholdadminflowui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
