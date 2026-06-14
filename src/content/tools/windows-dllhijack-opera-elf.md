---
trust_level: community
id: windows-dllhijack-opera-elf
namespace: windows:dllhijack:opera-elf
name: opera_elf.dll
description: "opera_elf.dll — Sideloading hijacking (Opera)"
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
  template: "opera_elf.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/ShitSecure/status/1566127363389329412"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/opera-elf.html"
---
examples:
  - description: "Place malicious opera_elf.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Programs\\Opera\\%VERSION%\\opera_elf.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\programs\\opera\\%VERSION%\\opera.exe\""

# opera_elf.dll

**Vendor:** Opera

**Expected Location:** %LOCALAPPDATA%\Programs\Opera\%VERSION%

**Vulnerable Executables:**
- %LOCALAPPDATA%\programs\opera\%VERSION%\opera.exe (Sideloading)

**Acknowledgement:** S3cur3Th1sSh1t
