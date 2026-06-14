---
trust_level: community
id: windows-dllhijack-mfc140u
namespace: windows:dllhijack:mfc140u
name: mfc140u.dll
description: "mfc140u.dll — Sideloading hijacking (CheckMAL)"
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
  template: "mfc140u.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/c4c85e98452094c8bd395b19c2afe283a50cdbb651e51e09d3f7b0dfa35fda65/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mfc140u.html"
---
examples:
  - description: "Place malicious mfc140u.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\CheckMAL\\AppCheck\\mfc140u.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\CheckMAL\\AppCheck\\AppCheck.exe\""

# mfc140u.dll

**Vendor:** CheckMAL

**Expected Location:** %PROGRAMFILES%\CheckMAL\AppCheck

**Vulnerable Executables:**
- %PROGRAMFILES%\CheckMAL\AppCheck\AppCheck.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Josh Allman
