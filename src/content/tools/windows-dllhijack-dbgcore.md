---
trust_level: community
id: windows-dllhijack-dbgcore
namespace: windows:dllhijack:dbgcore
name: dbgcore.dll
description: dbgcore.dll — Sideloading hijacking (Microsoft)
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
  template: dbgcore.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/dbgcore.html
features:
- requires-root
---

examples:
  - description: "Place malicious dbgcore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows kits\\10\\debuggers\\arm\\dbgcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\deploymentcsphelper.exe\""

# dbgcore.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows kits\10\debuggers\arm

**Vulnerable Executables:**
- %SYSTEM32%\deploymentcsphelper.exe (Sideloading)
- %SYSTEM32%\djoin.exe (Sideloading)
- %SYSTEM32%\dnscacheugc.exe (Sideloading)
- %SYSTEM32%\ieunatt.exe (Sideloading)
- %SYSTEM32%\muiunattend.exe (Sideloading)
- %SYSTEM32%\netbtugc.exe (Sideloading)
- %SYSTEM32%\netiougc.exe (Sideloading)
- %SYSTEM32%\pnpunattend.exe (Sideloading)
- %SYSTEM32%\setupugc.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\werfault.exe (Sideloading)
- %SYSTEM32%\werfaultsecure.exe (Sideloading)

**Acknowledgement:** Wietze
