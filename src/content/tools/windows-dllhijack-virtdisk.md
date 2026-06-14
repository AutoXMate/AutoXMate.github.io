---
trust_level: community
id: windows-dllhijack-virtdisk
namespace: windows:dllhijack:virtdisk
name: virtdisk.dll
description: virtdisk.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: virtdisk.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/virtdisk.html
features:
- local
---

examples:
  - description: "Place malicious virtdisk.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\virtdisk.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# virtdisk.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)

**Acknowledgement:** Wietze
