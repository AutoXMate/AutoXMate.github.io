---
trust_level: community
id: windows-dllhijack-hpbprndiloc
namespace: windows:dllhijack:hpbprndiloc
name: hpbprndiloc.dll
description: "hpbprndiloc.dll — Sideloading hijacking (HP)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "hpbprndiloc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://r136a1.dev/2026/01/14/command-and-evade-turlas-kazuar-v3-loader/"
  - label: "Reference"
    url: "https://github.com/TheEnergyStory/LoadLibraryControlFlowRedirection"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/hpbprndiloc.html"
---
examples:
  - description: "Place malicious hpbprndiloc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Hewlett-Packard\\%VERSION%\\hpbprndiloc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"hpbprndi.exe\""

# hpbprndiloc.dll

**Vendor:** HP

**Expected Location:** %PROGRAMFILES%\Hewlett-Packard\%VERSION%

**Vulnerable Executables:**
- hpbprndi.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
