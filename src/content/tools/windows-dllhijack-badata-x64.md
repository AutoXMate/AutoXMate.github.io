---
trust_level: community
id: windows-dllhijack-badata-x64
namespace: windows:dllhijack:badata-x64
name: badata_x64.dll
description: "badata_x64.dll — Sideloading hijacking (Glorylogic)"
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
  template: "badata_x64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/9326dd40e37d720f15a0104f89d6e76eb7a75b6e1fad14018326dbaa01681e74/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/badata-x64.html"
---
examples:
  - description: "Place malicious badata_x64.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\True Burner\\badata_x64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\True Burner\\TrueBurner.exe\""

# badata_x64.dll

**Vendor:** Glorylogic

**Expected Location:** %PROGRAMFILES%\True Burner

**Vulnerable Executables:**
- %PROGRAMFILES%\True Burner\TrueBurner.exe (Sideloading)

**Acknowledgement:** Jai Minton
