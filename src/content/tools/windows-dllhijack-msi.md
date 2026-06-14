---
trust_level: community
id: windows-dllhijack-msi
namespace: windows:dllhijack:msi
name: msi.dll
description: msi.dll — Sideloading hijacking (Microsoft)
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
  template: msi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/msi.html
features:
- requires-root
---

examples:
  - description: "Place malicious msi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dxpserver.exe\""

# msi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dxpserver.exe (Sideloading)
- %SYSTEM32%\fondue.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\msiexec.exe (Sideloading)
- %SYSTEM32%\optionalfeatures.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\packageinspector.exe (Sideloading)

**Acknowledgement:** Wietze
