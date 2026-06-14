---
trust_level: community
id: windows-dllhijack-tutil32
namespace: windows:dllhijack:tutil32
name: tutil32.dll
description: "tutil32.dll — Sideloading hijacking (mitec)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "tutil32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.mitec.cz/pde.html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tutil32.html"
---
examples:
  - description: "Place malicious tutil32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\PDE\\tutil32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\PDE\\PDE.exe\""

# tutil32.dll

**Vendor:** mitec

**Expected Location:** %PROGRAMFILES%\PDE

**Vulnerable Executables:**
- %PROGRAMFILES%\PDE\PDE.exe (Sideloading)

**Acknowledgement:** Jai Minton
