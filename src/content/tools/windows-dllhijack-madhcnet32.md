---
trust_level: community
id: windows-dllhijack-madhcnet32
namespace: windows:dllhijack:madhcnet32
name: madhcnet32.dll
description: "madhcnet32.dll — Sideloading hijacking (Systemsoftware Mathias Rauen)"
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
  template: "madhcnet32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d98677d4cf165a8885dc16e8a8411b36bfe39b10e188c6277253173b3ff73346/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/madhcnet32.html"
---
examples:
  - description: "Place malicious madhcnet32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Multimedia\\K-Lite Codec Pack\\Filters\\madVR\\madhcnet32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\K-Lite Codec Pack\\Filters\\madVR\\madHcCtrl.exe\""

# madhcnet32.dll

**Vendor:** Systemsoftware Mathias Rauen

**Expected Location:** %PROGRAMFILES%\Multimedia\K-Lite Codec Pack\Filters\madVR

**Vulnerable Executables:**
- %PROGRAMFILES%\K-Lite Codec Pack\Filters\madVR\madHcCtrl.exe (Sideloading)

**Acknowledgement:** Jai Minton
