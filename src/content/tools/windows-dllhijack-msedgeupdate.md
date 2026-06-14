---
trust_level: community
id: windows-dllhijack-msedgeupdate
namespace: windows:dllhijack:msedgeupdate
name: msedgeupdate.dll
description: msedgeupdate.dll — Sideloading hijacking (Microsoft)
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
  template: msedgeupdate.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: HijackLibs
  url: https://hijacklibs.net/entries/msedgeupdate.html
features:
- pipes-stdin
---

examples:
  - description: "Place malicious msedgeupdate.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft\\EdgeUpdate\\%VERSION%\\msedgeupdate.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe\""

# msedgeupdate.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft\EdgeUpdate\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe (Sideloading)

**Acknowledgement:** Still Hsu
