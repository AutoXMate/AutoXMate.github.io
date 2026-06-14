---
trust_level: community
id: windows-dllhijack-msedge-elf
namespace: windows:dllhijack:msedge-elf
name: msedge_elf.dll
description: msedge_elf.dll — Sideloading hijacking (Microsoft)
author: Still Hsu
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: msedge_elf.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.sentinelone.com/labs/chinese-entanglement-dll-hijacking-in-the-asian-gambling-sector/
- label: HijackLibs
  url: https://hijacklibs.net/entries/msedge-elf.html
features:
- pipes-stdin
---

examples:
  - description: "Place malicious msedge_elf.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft\\Edge\\Application\\%VERSION%\\msedge_elf.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft\\Edge\\Application\\%VERSION%\""

# msedge_elf.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft\Edge\Application\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft\Edge\Application\%VERSION% (Sideloading)

**Acknowledgement:** Still Hsu
