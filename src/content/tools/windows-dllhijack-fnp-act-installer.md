---
trust_level: community
id: windows-dllhijack-fnp-act-installer
namespace: windows:dllhijack:fnp-act-installer
name: fnp_act_installer.dll
description: "fnp_act_installer.dll — Sideloading hijacking (Flexera)"
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
  template: "fnp_act_installer.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e7b69768215453b2c648d7060161ce9b9eaf1ace631eb2ac11b60a7195e2263e"
  - label: "Reference"
    url: "https://app.any.run/tasks/faf0d668-7e06-4b1c-922b-2bb3a9d81dae"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fnp-act-installer.html"
---
examples:
  - description: "Place malicious fnp_act_installer.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\InstallShield\\%VERSION%\\System\\fnp_act_installer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\InstallShield\\%VERSION%\\System\\TSConfig.exe\""

# fnp_act_installer.dll

**Vendor:** Flexera

**Expected Location:** %PROGRAMFILES%\InstallShield\%VERSION%\System

**Vulnerable Executables:**
- %PROGRAMFILES%\InstallShield\%VERSION%\System\TSConfig.exe (Sideloading)
- %PROGRAMFILES%\InstallShield\%VERSION%\System\ISDbg.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Josh Allman
