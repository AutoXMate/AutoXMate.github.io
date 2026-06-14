---
trust_level: community
id: windows-dllhijack-archiveint
namespace: windows:dllhijack:archiveint
name: archiveint.dll
description: archiveint.dll — Sideloading hijacking (Microsoft)
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
  template: archiveint.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/archiveint.html
features:
- file-system
mitre_ids:
- T1560
---

examples:
  - description: "Place malicious archiveint.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\archiveint.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\tar.exe\""

# archiveint.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\tar.exe (Sideloading)

**Acknowledgement:** Wietze
