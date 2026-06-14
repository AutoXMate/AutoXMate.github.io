---
trust_level: community
id: windows-dllhijack-feclient
namespace: windows:dllhijack:feclient
name: feclient.dll
description: feclient.dll — Sideloading hijacking (Microsoft)
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
  template: feclient.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/feclient.html
features:
- remote
---

examples:
  - description: "Place malicious feclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\feclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cipher.exe\""

# feclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cipher.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)

**Acknowledgement:** Wietze
