---
trust_level: community
id: windows-dllhijack-asfbncor
namespace: windows:dllhijack:asfbncor
name: asfbncor.dll
description: "asfbncor.dll — Sideloading hijacking (Radioactive)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "asfbncor.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d1d824fc5f3354f68324a319026d089926655b6ce25538279e26c0986374026b/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/asfbncor.html"
---
examples:
  - description: "Place malicious asfbncor.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Replay Media Splitter\\asfbncor.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Replay Media Splitter\\ReplayMediaSplitter.exe\""

# asfbncor.dll

**Vendor:** Radioactive

**Expected Location:** %PROGRAMFILES%\Replay Media Splitter

**Vulnerable Executables:**
- %PROGRAMFILES%\Replay Media Splitter\ReplayMediaSplitter.exe (Sideloading)

**Acknowledgement:** Jai Minton
