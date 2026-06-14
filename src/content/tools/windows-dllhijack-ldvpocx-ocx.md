---
trust_level: community
id: windows-dllhijack-ldvpocx-ocx
namespace: windows:dllhijack:ldvpocx-ocx
name: ldvpocx.ocx.dll
description: "ldvpocx.ocx.dll — Sideloading hijacking (Symantec)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "ldvpocx.ocx.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox"
  - label: "Reference"
    url: "https://github.com/RedDrip7/APT_Digital_Weapon/blob/master/APT27/APT27_hash.md"
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ldvpocx-ocx.html"
---
examples:
  - description: "Place malicious ldvpocx.ocx.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Symantec_Client_Security\\Symantec AntiVirus\\ldvpocx.ocx.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Symantec_Client_Security\\Symantec AntiVirus\\ldvpreg.exe\""

# ldvpocx.ocx.dll

**Vendor:** Symantec

**Expected Location:** %PROGRAMFILES%\Symantec_Client_Security\Symantec AntiVirus

**Vulnerable Executables:**
- %PROGRAMFILES%\Symantec_Client_Security\Symantec AntiVirus\ldvpreg.exe (Sideloading)
