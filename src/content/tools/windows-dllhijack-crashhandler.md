---
trust_level: community
id: windows-dllhijack-crashhandler
namespace: windows:dllhijack:crashhandler
name: crashhandler.dll
description: "crashhandler.dll — Sideloading hijacking (Valve)"
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
  template: "crashhandler.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://x.com/AzakaSekai_/status/1991358486912069774"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/c4e3c29367426fe4ed718ab448fbdf2cf8690c81ea539805569cdff88317db9f"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/crashhandler.html"
---
examples:
  - description: "Place malicious crashhandler.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Steam\\crashhandler.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Steam\\bin\\steam_monitor.exe\""

# crashhandler.dll

**Vendor:** Valve

**Expected Location:** %PROGRAMFILES%\Steam

**Vulnerable Executables:**
- %PROGRAMFILES%\Steam\bin\steam_monitor.exe (Sideloading)

**Acknowledgement:** Still Hsu
