---
trust_level: community
id: windows-dllhijack-sqlite
namespace: windows:dllhijack:sqlite
name: sqlite.dll
description: "sqlite.dll — Sideloading hijacking (Adobe)"
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
  template: "sqlite.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/802bad293e5d5e75ffac3df3dd5301315a886534011871275a1b41c9cec1f298"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sqlite.html"
---
examples:
  - description: "Place malicious sqlite.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Adobe\\Acrobat Reader DC\\Reader\\sqlite.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Adobe\\Acrobat Reader DC\\Reader\\AcroBroker.exe\""

# sqlite.dll

**Vendor:** Adobe

**Expected Location:** %PROGRAMFILES%\Adobe\Acrobat Reader DC\Reader

**Vulnerable Executables:**
- %PROGRAMFILES%\Adobe\Acrobat Reader DC\Reader\AcroBroker.exe (Sideloading)

**Acknowledgement:** Jai Minton
