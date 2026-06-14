---
trust_level: community
id: windows-dllhijack-jrtools
namespace: windows:dllhijack:jrtools
name: jrtools.dll
description: "jrtools.dll — Sideloading hijacking (JRiver)"
author: "Rick Gatenby"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "jrtools.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://ventdrop.github.io/posts/jriver/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/jrtools.html"
---
examples:
  - description: "Place malicious jrtools.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\J River\\Media Center %VERSION%\\jrtools.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\J River\\Media Center %VERSION%\\JRService.exe\""

# jrtools.dll

**Vendor:** JRiver

**Expected Location:** %PROGRAMFILES%\J River\Media Center %VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\J River\Media Center %VERSION%\JRService.exe (Sideloading)

**Acknowledgement:** Rick Gatenby
