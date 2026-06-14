---
trust_level: community
id: windows-dllhijack-vsodscpl
namespace: windows:dllhijack:vsodscpl
name: vsodscpl.dll
description: vsodscpl.dll — Sideloading hijacking (McAfee)
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
  template: vsodscpl.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://eiploader.wordpress.com/2011/03/28/digitally-signed-malware-without-stealing-certificates/
- label: HijackLibs
  url: https://hijacklibs.net/entries/vsodscpl.html
features:
- file-system
---

examples:
  - description: "Place malicious vsodscpl.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\McAfee\\VirusScan Enterprise\\vsodscpl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"scncfg32.exe\""

# vsodscpl.dll

**Vendor:** McAfee

**Expected Location:** %PROGRAMFILES%\McAfee\VirusScan Enterprise

**Vulnerable Executables:**
- scncfg32.exe (Sideloading)

**Acknowledgement:** Sean Gallagher
