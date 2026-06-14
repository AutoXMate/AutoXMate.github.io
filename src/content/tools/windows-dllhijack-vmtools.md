---
trust_level: community
id: windows-dllhijack-vmtools
namespace: windows:dllhijack:vmtools
name: vmtools.dll
description: "vmtools.dll — Sideloading hijacking (VMWare)"
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
  template: "vmtools.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/a3d340480fc015cd7c548fccad9218222c37178af95727b612d768d8e4b24964/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vmtools.html"
---
examples:
  - description: "Place malicious vmtools.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VMware\\VMware Tools\\vmtools.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\VMware\\VMware Tools\\rvmSetup.exe\""

# vmtools.dll

**Vendor:** VMWare

**Expected Location:** %PROGRAMFILES%\VMware\VMware Tools

**Vulnerable Executables:**
- %PROGRAMFILES%\VMware\VMware Tools\rvmSetup.exe (Sideloading)

**Acknowledgement:** Jai Minton
