---
trust_level: community
id: windows-dllhijack-mcutil
namespace: windows:dllhijack:mcutil
name: mcutil.dll
description: mcutil.dll — Sideloading hijacking (McAfee)
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
  template: mcutil.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.virustotal.com/gui/file/3bcb28d19a779b6da0c42c1506cd1908f9bcceeffff45f572677e032551f9a96/relations
- label: Reference
  url: https://www.virustotal.com/gui/file/b0263de0622050091a0fbf06428229e5da291b87926ca29c8ee3b01a2a514e4f/detection
- label: Reference
  url: https://web-assets.esetstatic.com/wls/2018/03/ESET_OceanLotus.pdf
- label: Reference
  url: https://www.huntress.com/blog/advanced-persistent-threat-targeting-vietnamese-human-rights-defenders
- label: HijackLibs
  url: https://hijacklibs.net/entries/mcutil.html
features:
- pipes-stdin
---

examples:
  - description: "Place malicious mcutil.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\McAfee Inc.\\McAfee Total Protection 2009\\mcutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"mcoemcpy.exe\""

# mcutil.dll

**Vendor:** McAfee

**Expected Location:** %PROGRAMFILES%\McAfee Inc.\McAfee Total Protection 2009

**Vulnerable Executables:**
- mcoemcpy.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Craig Sweeney
