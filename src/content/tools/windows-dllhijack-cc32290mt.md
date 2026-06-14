---
trust_level: community
id: windows-dllhijack-cc32290mt
namespace: windows:dllhijack:cc32290mt
name: cc32290mt.dll
description: "cc32290mt.dll — Sideloading hijacking (Ahnenblatt)"
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
  template: "cc32290mt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/dab744a533bcbc4a2d3f19a54694ceb00587a0ce68d046ca9085d5013321ea5a"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cc32290mt.html"
---
examples:
  - description: "Place malicious cc32290mt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Ahnenblatt4\\Ahnenblatt4.exe\\cc32290mt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Ahnenblatt4\\Ahnenblatt4.exe\""

# cc32290mt.dll

**Vendor:** Ahnenblatt

**Expected Location:** %PROGRAMFILES%\Ahnenblatt4\Ahnenblatt4.exe

**Vulnerable Executables:**
- %PROGRAMFILES%\Ahnenblatt4\Ahnenblatt4.exe (Sideloading)

**Acknowledgement:** Josh Allman

**Acknowledgement:** Amelia Casley

**Acknowledgement:** Faith Stratton
