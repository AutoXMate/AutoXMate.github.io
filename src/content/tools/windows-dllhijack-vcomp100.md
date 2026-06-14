---
trust_level: community
id: windows-dllhijack-vcomp100
namespace: windows:dllhijack:vcomp100
name: vcomp100.dll
description: "vcomp100.dll — Sideloading hijacking (Adobe)"
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
  template: "vcomp100.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/0ab581841cc19922d424dbc518d279070ea75ec2983334ba1b74c16ca5729bc1/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/5a5e1142b50096e3af0f9079c45c84f8a6ca1be60e45dbc489327a2632d73fd5/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vcomp100.html"
---
examples:
  - description: "Place malicious vcomp100.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\vcomp100.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Adobe\\Adobe Photoshop %VERSION%\\convert.exe\""

# vcomp100.dll

**Vendor:** Adobe

**Vulnerable Executables:**
- %PROGRAMFILES%\Adobe\Adobe Photoshop %VERSION%\convert.exe (Sideloading)

**Acknowledgement:** Jai Minton
