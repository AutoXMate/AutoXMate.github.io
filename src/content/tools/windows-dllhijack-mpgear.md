---
trust_level: community
id: windows-dllhijack-mpgear
namespace: windows:dllhijack:mpgear
name: mpgear.dll
description: "mpgear.dll — Sideloading hijacking (Microsoft)"
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
  template: "mpgear.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/1643a9c54e5d730fb0ebf4ab49e6c1d3a09dcd2c3a0282674330346d90990ab0"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e1316301e7904a415fdd2a1707d1a48220cce055aab17b36a48e67bf0369edba"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mpgear.html"
---
examples:
  - description: "Place malicious mpgear.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Defender Advanced Threat Protection\\Classification\\mpgear.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Defender Advanced Threat Protection\\Classification\\SenseCE.exe\""

# mpgear.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Defender Advanced Threat Protection\Classification

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Defender Advanced Threat Protection\Classification\SenseCE.exe (Sideloading)

**Acknowledgement:** Jai Minton
