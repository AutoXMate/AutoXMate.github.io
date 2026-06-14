---
trust_level: community
id: windows-dllhijack-uxcore
namespace: windows:dllhijack:uxcore
name: uxcore.dll
description: "uxcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "uxcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/016468b087cdbe5123189b68965cb65dc95ba1a59fc3ed32144b92d1274d13b6/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/23c3fec8dc60c06caadecb31e2d770212e70faf0de866cb5878622f077d4fe2a"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uxcore.html"
---
examples:
  - description: "Place malicious uxcore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows live\\installer\\uxcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\windows live\\installer\\Dashboard.exe\""

# uxcore.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows live\installer

**Vulnerable Executables:**
- %PROGRAMFILES%\windows live\installer\Dashboard.exe (Sideloading)

**Acknowledgement:** Jai Minton
