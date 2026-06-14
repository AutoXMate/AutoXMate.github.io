---
trust_level: community
id: windows-dllhijack-fveapi
namespace: windows:dllhijack:fveapi
name: fveapi.dll
description: fveapi.dll — Sideloading hijacking (Microsoft)
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
  template: fveapi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/fveapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious fveapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fveapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\baaupdate.exe\""

# fveapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\baaupdate.exe (Sideloading)
- %SYSTEM32%\bdechangepin.exe (Sideloading)
- %SYSTEM32%\fvenotify.exe (Sideloading)
- %SYSTEM32%\fveprompt.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
