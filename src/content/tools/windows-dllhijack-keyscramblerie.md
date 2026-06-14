---
trust_level: community
id: windows-dllhijack-keyscramblerie
namespace: windows:dllhijack:keyscramblerie
name: keyscramblerie.dll
description: "keyscramblerie.dll — Sideloading hijacking (QFX)"
author: "Matt Anderson - HuntressLabs, Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "keyscramblerie.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://thehackernews.com/2024/03/two-chinese-apt-groups-ramp-up-cyber.html"
  - label: "Reference"
    url: "https://csirt-cti.net/2024/02/01/stately-taurus-continued-new-information-on-cyberespionage-attacks-against-myanmar-military-junta/"
  - label: "Reference"
    url: "https://bazaar.abuse.ch/sample/5cb9876681f78d3ee8a01a5aaa5d38b05ec81edc48b09e3865b75c49a2187831/"
  - label: "Reference"
    url: "https://twitter.com/Max_Mal_/status/1775222576639291859"
  - label: "Reference"
    url: "https://twitter.com/DTCERT/status/1712785426895839339"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/5cb9876681f78d3ee8a01a5aaa5d38b05ec81edc48b09e3865b75c49a2187831/details"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/9cfdc3fe2a10fe2b514fc224c9c8740e1de039d90b9c17f85b64ff29d4a4ebb1"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/keyscramblerie.html"
---
examples:
  - description: "Place malicious keyscramblerie.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\KeyScrambler\\keyscramblerie.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\KeyScrambler\\KeyScrambler.exe\""

# keyscramblerie.dll

**Vendor:** QFX

**Expected Location:** %PROGRAMFILES%\KeyScrambler

**Vulnerable Executables:**
- %PROGRAMFILES%\KeyScrambler\KeyScrambler.exe (Sideloading)

**Acknowledgement:** Matt Anderson

**Acknowledgement:** Swachchhanda Shrawan Poudel
