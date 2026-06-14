---
trust_level: community
id: windows-dllhijack-cc3260mt
namespace: windows:dllhijack:cc3260mt
name: cc3260mt.dll
description: "cc3260mt.dll — Sideloading hijacking (TiVo)"
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
  template: "cc3260mt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/3d8181ea38667550d141f813372b2d7bae7b7f43cdc17e24688d72be97751505/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cc3260mt.html"
---
examples:
  - description: "Place malicious cc3260mt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\TiVo\\Desktop\\cc3260mt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\TiVo\\Desktop\\TiVoServer.exe\""

# cc3260mt.dll

**Vendor:** TiVo

**Expected Location:** %PROGRAMFILES%\TiVo\Desktop

**Vulnerable Executables:**
- %PROGRAMFILES%\TiVo\Desktop\TiVoServer.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Josh Allman
