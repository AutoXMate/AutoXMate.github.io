---
trust_level: community
id: windows-dllhijack-mspgimme
namespace: windows:dllhijack:mspgimme
name: mspgimme.dll
description: "mspgimme.dll — Sideloading hijacking (Microsoft)"
author: "Josh Allman"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "mspgimme.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mspgimme.html"
---
examples:
  - description: "Place malicious mspgimme.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Common Files\\Microsoft Shared\\MODI\\11.0\\mspgimme.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Common Files\\Microsoft Shared\\MODI\\11.0\\MSPSCAN.EXE\""

# mspgimme.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Common Files\Microsoft Shared\MODI\11.0

**Vulnerable Executables:**
- %PROGRAMFILES%\Common Files\Microsoft Shared\MODI\11.0\MSPSCAN.EXE (Sideloading)

**Acknowledgement:** Josh Allman

**Acknowledgement:** Jamie Dumas

**Acknowledgement:** Jevon Ang
