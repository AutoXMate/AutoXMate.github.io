---
trust_level: community
id: windows-dllhijack-msedge
namespace: windows:dllhijack:msedge
name: msedge.dll
description: "msedge.dll — Sideloading hijacking (Microsoft)"
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
  template: "msedge.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securelist.com/apt41-in-africa/116986/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msedge.html"
---
examples:
  - description: "Place malicious msedge.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft\\Edge\\Application\\%VERSION%\\msedge.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft\\Edge\\Application\\%VERSION%\\cookie_exporter.exe\""

# msedge.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft\Edge\Application\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft\Edge\Application\%VERSION%\cookie_exporter.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
