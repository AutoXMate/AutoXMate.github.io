---
trust_level: community
id: windows-dllhijack-mrmcorer
namespace: windows:dllhijack:mrmcorer
name: mrmcorer.dll
description: mrmcorer.dll — Sideloading hijacking (Microsoft)
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
  template: mrmcorer.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/mrmcorer.html
features:
- file-system
---

examples:
  - description: "Place malicious mrmcorer.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mrmcorer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mcbuilder.exe\""

# mrmcorer.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mcbuilder.exe (Sideloading)

**Acknowledgement:** Wietze
