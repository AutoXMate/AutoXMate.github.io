---
trust_level: community
id: windows-dllhijack-vboxrt
namespace: windows:dllhijack:vboxrt
name: vboxrt.dll
description: "vboxrt.dll — Sideloading hijacking (Oracle)"
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
  template: "vboxrt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/cf801023465679ec34084bdb1adb9f54b2fc3130925a4b8fdc10b11639b4a7cd"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vboxrt.html"
---
examples:
  - description: "Place malicious vboxrt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Oracle\\VirtualBox\\vboxrt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Oracle\\VirtualBox\\VBoxSVC.exe\""

# vboxrt.dll

**Vendor:** Oracle

**Expected Location:** %PROGRAMFILES%\Oracle\VirtualBox

**Vulnerable Executables:**
- %PROGRAMFILES%\Oracle\VirtualBox\VBoxSVC.exe (Sideloading)

**Acknowledgement:** Jai Minton
