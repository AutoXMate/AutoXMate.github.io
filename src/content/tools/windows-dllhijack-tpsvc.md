---
trust_level: community
id: windows-dllhijack-tpsvc
namespace: windows:dllhijack:tpsvc
name: tpsvc.dll
description: "tpsvc.dll — Sideloading hijacking (ThinPrint)"
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
  template: "tpsvc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/cf801023465679ec34084bdb1adb9f54b2fc3130925a4b8fdc10b11639b4a7cd"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/a6e6b1a47021fa1e4d36b047f5326eb04d5f545907fc6ac3730162a07cc792ff"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tpsvc.html"
---
examples:
  - description: "Place malicious tpsvc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VMWare\\VMWare Tools\\tpsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"TPAutoConnect.exe\""

# tpsvc.dll

**Vendor:** ThinPrint

**Expected Location:** %PROGRAMFILES%\VMWare\VMWare Tools

**Vulnerable Executables:**
- TPAutoConnect.exe (Sideloading)

**Acknowledgement:** Jai Minton
