---
trust_level: community
id: windows-dllhijack-printui
namespace: windows:dllhijack:printui
name: printui.dll
description: printui.dll — Sideloading hijacking (Microsoft)
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
  template: printui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/printui.html
features:
- pipes-stdout
- requires-root
---

examples:
  - description: "Place malicious printui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\printui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\printui.exe\""

# printui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\printui.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
