---
trust_level: community
id: windows-dllhijack-avutil
namespace: windows:dllhijack:avutil
name: avutil.dll
description: "avutil.dll — Sideloading hijacking (VSO Software)"
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
  template: "avutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/Tac_Mangusta/status/1807778398887928313"
  - label: "Reference"
    url: "https://www.joesandbox.com/analysis/1357123/0/html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/avutil.html"
---
examples:
  - description: "Place malicious avutil.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VSO\\ConvertX\\7\\avutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\VSO\\ConvertX\\7\\ConvertXToDVD.exe\""

# avutil.dll

**Vendor:** VSO Software

**Expected Location:** %PROGRAMFILES%\VSO\ConvertX\7

**Vulnerable Executables:**
- %PROGRAMFILES%\VSO\ConvertX\7\ConvertXToDVD.exe (Sideloading)

**Acknowledgement:** Mangusta
