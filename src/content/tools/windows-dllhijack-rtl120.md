---
trust_level: community
id: windows-dllhijack-rtl120
namespace: windows:dllhijack:rtl120
name: rtl120.dll
description: rtl120.dll — Sideloading hijacking (iTop)
author: Jai Minton - HuntressLabs
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: rtl120.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.virustotal.com/gui/file/0e93a41edf1ca3e1723e5e0d73f3e0f54d6d672606b9dc0cda745f87e3fd0339/relations
- label: Reference
  url: https://www.virustotal.com/gui/file/6028d64b53880676fcd62b445fd71952f9141b8ac0e60329b15cf9e04e437cea/details
- label: HijackLibs
  url: https://hijacklibs.net/entries/rtl120.html
features:
- process-manip
---

examples:
  - description: "Place malicious rtl120.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\DualSafe Password Manager\\rtl120.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\DualSafe Password Manager\\DPMInit.exe\""

# rtl120.dll

**Vendor:** iTop

**Expected Location:** %PROGRAMFILES%\DualSafe Password Manager

**Vulnerable Executables:**
- %PROGRAMFILES%\DualSafe Password Manager\DPMInit.exe (Sideloading)

**Acknowledgement:** Jai Minton
