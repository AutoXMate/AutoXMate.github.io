---
trust_level: community
id: windows-dllhijack-shfolder
namespace: windows:dllhijack:shfolder
name: shfolder.dll
description: "shfolder.dll — Sideloading hijacking (VMWare)"
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
  template: "shfolder.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/dissectmalware/status/978017957480628226"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/shfolder.html"
---
examples:
  - description: "Place malicious shfolder.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\shfolder.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\VMNat.exe\""

# shfolder.dll

**Vendor:** VMWare

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\VMNat.exe (Sideloading)
