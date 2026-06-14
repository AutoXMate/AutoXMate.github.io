---
trust_level: community
id: windows-dllhijack-asio
namespace: windows:dllhijack:asio
name: asio.dll
description: "asio.dll — Sideloading hijacking (Asus)"
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
  template: "asio.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/006f91524d53d483074335f74c2ca2c10cab9b64de86f6151eedfa53174434f2/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/7f4689de97d97ddb6e788119ebf0dc3707c66f8216d7cbc79ea329d0c3df63bf/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/asio.html"
---
examples:
  - description: "Place malicious asio.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\ASUS\\AXSP\\%VERSION%\\asio.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\ASUS\\AXSP\\4.02.12\\atkexComSvc.exe\""

# asio.dll

**Vendor:** Asus

**Expected Location:** %PROGRAMFILES%\ASUS\AXSP\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\ASUS\AXSP\4.02.12\atkexComSvc.exe (Sideloading)

**Acknowledgement:** Jai Minton
