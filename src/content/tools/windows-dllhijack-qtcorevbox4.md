---
trust_level: community
id: windows-dllhijack-qtcorevbox4
namespace: windows:dllhijack:qtcorevbox4
name: qtcorevbox4.dll
description: "qtcorevbox4.dll — Sideloading hijacking (Oracle)"
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
  template: "qtcorevbox4.dll"
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
    url: "https://hijacklibs.net/entries/qtcorevbox4.html"
---
examples:
  - description: "Place malicious qtcorevbox4.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Oracle\\VirtualBox\\qtcorevbox4.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Oracle\\VirtualBox\\VBoxTestOGL.exe\""

# qtcorevbox4.dll

**Vendor:** Oracle

**Expected Location:** %PROGRAMFILES%\Oracle\VirtualBox

**Vulnerable Executables:**
- %PROGRAMFILES%\Oracle\VirtualBox\VBoxTestOGL.exe (Sideloading)

**Acknowledgement:** Jai Minton
