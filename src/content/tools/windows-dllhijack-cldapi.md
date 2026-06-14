---
trust_level: community
id: windows-dllhijack-cldapi
namespace: windows:dllhijack:cldapi
name: cldapi.dll
description: cldapi.dll — Sideloading hijacking (Microsoft)
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
  template: cldapi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/cldapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious cldapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cldapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# cldapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\resmon.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Wietze
