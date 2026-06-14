---
trust_level: community
id: windows-dllhijack-bcp47langs
namespace: windows:dllhijack:bcp47langs
name: bcp47langs.dll
description: bcp47langs.dll — Sideloading hijacking (Microsoft)
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
  template: bcp47langs.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/bcp47langs.html
features:
- file-system
- requires-root
---

examples:
  - description: "Place malicious bcp47langs.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bcp47langs.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\lpremove.exe\""

# bcp47langs.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\lpremove.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
