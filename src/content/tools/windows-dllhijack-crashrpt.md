---
trust_level: community
id: windows-dllhijack-crashrpt
namespace: windows:dllhijack:crashrpt
name: crashrpt.dll
description: "crashrpt.dll — Sideloading hijacking (Idol)"
author: "Still Hsu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "crashrpt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/db35155d33b616d4f7c268e78c8179eb84378778a4b195df09a8c36f2e5eb38b"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/crashrpt.html"
---
examples:
  - description: "Place malicious crashrpt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\MPC-HC\\CrashReporter\\crashrpt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\MPC-HC\\mpc-hc.exe\""

# crashrpt.dll

**Vendor:** Idol

**Expected Location:** %PROGRAMFILES%\MPC-HC\CrashReporter

**Vulnerable Executables:**
- %PROGRAMFILES%\MPC-HC\mpc-hc.exe (Sideloading)
- %PROGRAMFILES%\MPC-HC\mpc-hc64.exe (Sideloading)
