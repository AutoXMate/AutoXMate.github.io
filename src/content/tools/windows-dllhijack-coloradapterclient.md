---
trust_level: community
id: windows-dllhijack-coloradapterclient
namespace: windows:dllhijack:coloradapterclient
name: coloradapterclient.dll
description: coloradapterclient.dll — Sideloading hijacking (Microsoft)
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
  template: coloradapterclient.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/coloradapterclient.html
features:
- remote
- requires-root
---

examples:
  - description: "Place malicious coloradapterclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\coloradapterclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\colorcpl.exe\""

# coloradapterclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\colorcpl.exe (Sideloading)
- %SYSTEM32%\dccw.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
