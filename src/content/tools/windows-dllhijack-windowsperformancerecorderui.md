---
trust_level: community
id: windows-dllhijack-windowsperformancerecorderui
namespace: windows:dllhijack:windowsperformancerecorderui
name: windowsperformancerecorderui.dll
description: windowsperformancerecorderui.dll — Sideloading hijacking (Microsoft)
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
  template: windowsperformancerecorderui.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/
- label: HijackLibs
  url: https://hijacklibs.net/entries/windowsperformancerecorderui.html
features:
- file-system
- requires-root
---

examples:
  - description: "Place malicious windowsperformancerecorderui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\10\\Windows Performance Toolkit\\windowsperformancerecorderui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\Windows Performance Toolkit\\WPRUI.exe\""

# windowsperformancerecorderui.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\10\Windows Performance Toolkit

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\Windows Performance Toolkit\WPRUI.exe (Sideloading) [AutoElevate]
