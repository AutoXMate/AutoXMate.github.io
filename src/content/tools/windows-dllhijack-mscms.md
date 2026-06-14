---
trust_level: community
id: windows-dllhijack-mscms
namespace: windows:dllhijack:mscms
name: mscms.dll
description: mscms.dll — Sideloading hijacking (Microsoft)
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
  template: mscms.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/mscms.html
features:
- requires-root
---

examples:
  - description: "Place malicious mscms.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mscms.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\colorcpl.exe\""

# mscms.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\colorcpl.exe (Sideloading)
- %SYSTEM32%\dccw.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
