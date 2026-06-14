---
trust_level: community
id: windows-dllhijack-gflagsui
namespace: windows:dllhijack:gflagsui
name: gflagsui.dll
description: gflagsui.dll — Sideloading hijacking (Microsoft)
author: Gary Lobermier
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
  template: gflagsui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/
- label: HijackLibs
  url: https://hijacklibs.net/entries/gflagsui.html
features:
- requires-root
---

examples:
  - description: "Place malicious gflagsui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\10\\Debuggers\\%VERSION%\\gflagsui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\Debuggers\\%VERSION%\\gflags.exe\""

# gflagsui.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\10\Debuggers\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\Debuggers\%VERSION%\gflags.exe (Sideloading) [AutoElevate]
