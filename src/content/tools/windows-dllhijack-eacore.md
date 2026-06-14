---
trust_level: community
id: windows-dllhijack-eacore
namespace: windows:dllhijack:eacore
name: eacore.dll
description: "eacore.dll — Sideloading hijacking (Electronic Arts)"
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
  template: "eacore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/"
  - label: "Reference"
    url: "https://x.com/FatzQatz/status/1883443770819248130"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/dc673d59a6a9df3d02e83fd03af80e117bea20954602ae416540870b1b3d13c4"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/eacore.html"
---
examples:
  - description: "Place malicious eacore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Electronic Arts\\EA Desktop\\EA Desktop\\eacore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Electronic Arts\\EA Desktop\\EA Desktop\\EACoreServer.exe\""

# eacore.dll

**Vendor:** Electronic Arts

**Expected Location:** %PROGRAMFILES%\Electronic Arts\EA Desktop\EA Desktop

**Vulnerable Executables:**
- %PROGRAMFILES%\Electronic Arts\EA Desktop\EA Desktop\EACoreServer.exe (Sideloading)

**Acknowledgement:** FatzQatz
