---
trust_level: community
id: windows-dllhijack-textshaping
namespace: windows:dllhijack:textshaping
name: textshaping.dll
description: textshaping.dll — Sideloading hijacking (Microsoft)
author: Gary Lobermier
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: textshaping.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/
- label: HijackLibs
  url: https://hijacklibs.net/entries/textshaping.html
features:
- network-intensive
---

examples:
  - description: "Place malicious textshaping.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\textshaping.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\Debuggers\\x64\\logger.exe\""

# textshaping.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\Debuggers\x64\logger.exe (Sideloading)
- %PROGRAMFILES%\Windows Kits\10\Debuggers\x64\logviewer.exe (Sideloading)
