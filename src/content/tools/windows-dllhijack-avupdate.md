---
trust_level: community
id: windows-dllhijack-avupdate
namespace: windows:dllhijack:avupdate
name: avupdate.dll
description: "avupdate.dll — Sideloading hijacking (Carbon Black)"
author: "Josh Allman"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "avupdate.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blackpointcyber.com/resources/blog/qilin-ransomware-and-the-hidden-dangers-of-byovd/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/avupdate.html"
---
examples:
  - description: "Place malicious avupdate.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Confer\\scanner\\upd.exe\\avupdate.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Confer\\scanner\\upd.exe\""

# avupdate.dll

**Vendor:** Carbon Black

**Expected Location:** %PROGRAMFILES%\Confer\scanner\upd.exe

**Vulnerable Executables:**
- %PROGRAMFILES%\Confer\scanner\upd.exe (Sideloading)

**Acknowledgement:** Josh Allman
