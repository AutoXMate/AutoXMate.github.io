---
trust_level: community
id: windows-dllhijack-libxfont-1
namespace: windows:dllhijack:libxfont-1
name: libxfont-1.dll
description: "libxfont-1.dll — Sideloading hijacking (Mobatek)"
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
  template: "libxfont-1.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/b99bd7ffb7634749487570d0b3a7e423047de4ab13a10c2d912660aec322618e/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libxfont-1.html"
---
examples:
  - description: "Place malicious libxfont-1.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Mobatek\\MobaXterm Personal Edition\\libxfont-1.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Mobatek\\MobaXterm Personal Edition\\MobaXterm.exe\""

# libxfont-1.dll

**Vendor:** Mobatek

**Expected Location:** %PROGRAMFILES%\Mobatek\MobaXterm Personal Edition

**Vulnerable Executables:**
- %PROGRAMFILES%\Mobatek\MobaXterm Personal Edition\MobaXterm.exe (Sideloading)
- %PROGRAMFILES%\Mobatek\MobaXterm\MobaXterm.exe (Sideloading)

**Acknowledgement:** Jai Minton
