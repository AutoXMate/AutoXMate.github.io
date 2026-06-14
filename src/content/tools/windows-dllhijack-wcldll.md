---
trust_level: community
id: windows-dllhijack-wcldll
namespace: windows:dllhijack:wcldll
name: wcldll.dll
description: "wcldll.dll — Sideloading hijacking (Cisco)"
author: "Jai Minton - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wcldll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/26227914bdad9baf491a9b966e6301fc997cff35c677dcfd9628654f4f6bc9fc/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/fa1443219f210bdcf3a25b311342851f61378536eb11810366468156fbd5c051"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wcldll.html"
---
examples:
  - description: "Place malicious wcldll.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Cisco Systems\\Cisco Jabber\\wcldll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Webex\\Applications\\ptInst.exe\""

# wcldll.dll

**Vendor:** Cisco

**Expected Location:** %PROGRAMFILES%\Cisco Systems\Cisco Jabber

**Vulnerable Executables:**
- %PROGRAMFILES%\Webex\Applications\ptInst.exe (Sideloading)

**Acknowledgement:** Jai Minton
