---
trust_level: community
id: windows-dllhijack-msimg32
namespace: windows:dllhijack:msimg32
name: msimg32.dll
description: "msimg32.dll — Sideloading hijacking (Microsoft)"
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
  template: "msimg32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/2f08e2316a38da2d39d31131a0e3314024ab80756050624afafc1e17b0562d5e/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msimg32.html"
---
examples:
  - description: "Place malicious msimg32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Haihaisoft PDF Reader\\msimg32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Haihaisoft PDF Reader\\hpreader.exe\""

# msimg32.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Haihaisoft PDF Reader

**Vulnerable Executables:**
- %PROGRAMFILES%\Haihaisoft PDF Reader\hpreader.exe (Sideloading)

**Acknowledgement:** Jai Minton
