---
trust_level: community
id: windows-dllhijack-edputil
namespace: windows:dllhijack:edputil
name: edputil.dll
description: "edputil.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
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
  template: "edputil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://twitter.com/Max_Mal_/status/1658566665003585545"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/edputil.html"
---
examples:
  - description: "Place malicious edputil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\edputil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\calc.exe\""

# edputil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\dpiscaling.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\mobsync.exe (Sideloading)
- %SYSTEM32%\resmon.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Wietze
