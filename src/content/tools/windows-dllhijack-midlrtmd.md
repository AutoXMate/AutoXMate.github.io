---
trust_level: community
id: windows-dllhijack-midlrtmd
namespace: windows:dllhijack:midlrtmd
name: midlrtmd.dll
description: "midlrtmd.dll — Sideloading hijacking (Microsoft)"
author: "Rick Gatenby"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "midlrtmd.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.crowdstrike.com/en-us/blog/new-supply-chain-attack-leverages-comm100-chat-installer"
  - label: "Reference"
    url: "https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_1_7_hara_nakajima_kawakami_en.pdf"
  - label: "Reference"
    url: "https://x.com/Cyberteam008/status/1858703453981450712"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/midlrtmd.html"
---
examples:
  - description: "Place malicious midlrtmd.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\%VERSION%\\bin\\%VERSION%\\x64\\mdmerge.exe\\midlrtmd.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"mdmerge.exe\""

# midlrtmd.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\%VERSION%\bin\%VERSION%\x64\mdmerge.exe

**Vulnerable Executables:**
- mdmerge.exe (Sideloading)

**Acknowledgement:** Rick Gatenby
