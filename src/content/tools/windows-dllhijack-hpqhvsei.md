---
trust_level: community
id: windows-dllhijack-hpqhvsei
namespace: windows:dllhijack:hpqhvsei
name: hpqhvsei.dll
description: "hpqhvsei.dll — Sideloading hijacking (HP)"
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
  template: "hpqhvsei.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://www.welivesecurity.com/2020/01/31/winnti-group-targeting-universities-hong-kong/"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/hpqhvsei.html"
---
examples:
  - description: "Place malicious hpqhvsei.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\HP\\hpqhvsei.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"hpqhvind.exe\""

# hpqhvsei.dll

**Vendor:** HP

**Expected Location:** %PROGRAMFILES%\HP

**Vulnerable Executables:**
- hpqhvind.exe (Sideloading)

**Acknowledgement:** Adam
