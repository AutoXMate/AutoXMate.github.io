---
trust_level: community
id: windows-dllhijack-qt5core
namespace: windows:dllhijack:qt5core
name: qt5core.dll
description: "qt5core.dll — Sideloading hijacking (Qt)"
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
  template: "qt5core.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/2251e6582a12427b9b70d0e9ec7c8c27debe22b0a08b6ff6be46f4fb8914338c"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/173e138d5cf12f7eb55a67bcf3afc97ac1d7598fe4290ca4f125f28692e90fed"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/qt5core.html"
---
examples:
  - description: "Place malicious qt5core.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Electronic Arts\\EA Desktop\\EA Desktop\\qt5core.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Electronic Arts\\EA Desktop\\EA Desktop\\EASteamProxy.exe\""

# qt5core.dll

**Vendor:** Qt

**Expected Location:** %PROGRAMFILES%\Electronic Arts\EA Desktop\EA Desktop

**Vulnerable Executables:**
- %PROGRAMFILES%\Electronic Arts\EA Desktop\EA Desktop\EASteamProxy.exe (Sideloading)

**Acknowledgement:** Jai Minton
