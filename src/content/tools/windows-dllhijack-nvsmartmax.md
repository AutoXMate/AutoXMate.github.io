---
trust_level: community
id: windows-dllhijack-nvsmartmax
namespace: windows:dllhijack:nvsmartmax
name: nvsmartmax.dll
description: "nvsmartmax.dll — Sideloading hijacking (Nvidia)"
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
  template: "nvsmartmax.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.cybereason.com/blog/research/deadringer-exposing-chinese-threat-actors-targeting-major-telcos"
  - label: "Reference"
    url: "https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/nvsmartmax.html"
---
examples:
  - description: "Place malicious nvsmartmax.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\NVIDIA Corporation\\Display\\nvsmartmax.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\NVIDIA Corporation\\Display\\nvSmartEx.exe\""

# nvsmartmax.dll

**Vendor:** Nvidia

**Expected Location:** %PROGRAMFILES%\NVIDIA Corporation\Display

**Vulnerable Executables:**
- %PROGRAMFILES%\NVIDIA Corporation\Display\nvSmartEx.exe (Sideloading)
