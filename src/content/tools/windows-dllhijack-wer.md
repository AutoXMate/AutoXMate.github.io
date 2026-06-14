---
trust_level: community
id: windows-dllhijack-wer
namespace: windows:dllhijack:wer
name: wer.dll
description: "wer.dll — Sideloading hijacking (Microsoft)"
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
  template: "wer.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wer.html"
---
examples:
  - description: "Place malicious wer.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dwwin.exe\""

# wer.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dwwin.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\pcalua.exe (Sideloading)
- %SYSTEM32%\relpost.exe (Sideloading)
- %SYSTEM32%\rstrui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\srtasks.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)
- %SYSTEM32%\werfault.exe (Sideloading)
- %SYSTEM32%\werfaultsecure.exe (Sideloading)
- %SYSTEM32%\wermgr.exe (Sideloading)

**Acknowledgement:** Wietze
