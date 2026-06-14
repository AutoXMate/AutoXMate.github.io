---
trust_level: community
id: windows-dllhijack-ci
namespace: windows:dllhijack:ci
name: ci.dll
description: "ci.dll — Sideloading hijacking (Digiarty)"
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
  template: "ci.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/2560b7390da7c7a1d92050d9c1f5e3a8025cd35fff5360fe73583b5e3f48731e"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/ae2453d0e03d72759d5239dcfe9518d6a721319006613a41f8bb53d37d4d1391/details"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/7306316b53f915aaff06f00896829884db857b7e5c2747188ae080cad5b8c0e1"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ci.html"
---
examples:
  - description: "Place malicious ci.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Digiarty\\WinX Blu-ray Decrypter\\ci.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Digiarty\\WinX Blu-ray Decrypter\\WinX Blu-ray Decrypter.exe\""

# ci.dll

**Vendor:** Digiarty

**Expected Location:** %PROGRAMFILES%\Digiarty\WinX Blu-ray Decrypter

**Vulnerable Executables:**
- %PROGRAMFILES%\Digiarty\WinX Blu-ray Decrypter\WinX Blu-ray Decrypter.exe (Sideloading)

**Acknowledgement:** Jai Minton
