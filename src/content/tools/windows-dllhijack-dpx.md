---
trust_level: community
id: windows-dllhijack-dpx
namespace: windows:dllhijack:dpx
name: dpx.dll
description: dpx.dll — Sideloading hijacking (Microsoft)
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
  template: dpx.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/dpx.html
features:
- requires-root
---

examples:
  - description: "Place malicious dpx.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dpx.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\lpksetup.exe\""

# dpx.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\lpksetup.exe (Sideloading)
- %SYSTEM32%\wusa.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
