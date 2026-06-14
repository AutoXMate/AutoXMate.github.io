---
trust_level: community
id: windows-dllhijack-zlibwapi
namespace: windows:dllhijack:zlibwapi
name: zlibwapi.dll
description: "zlibwapi.dll — Sideloading hijacking (zlib)"
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
  template: "zlibwapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/malwrhunterteam/status/1859316170773397966"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/b8d38fc9f4560719fa64227e4b25b732b22602cb596d44cb38418a196c3340be"
  - label: "Reference"
    url: "https://github.com/Still34/malware-lab/tree/main/reworkshop/2024-11-24"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/zlibwapi.html"
---
examples:
  - description: "Place malicious zlibwapi.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\DS Clock\\zlibwapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\DS Clock\\dsclock.exe\""

# zlibwapi.dll

**Vendor:** zlib

**Expected Location:** %PROGRAMFILES%\DS Clock

**Vulnerable Executables:**
- %PROGRAMFILES%\DS Clock\dsclock.exe (Sideloading)

**Acknowledgement:** MalwareHunterTeam

**Acknowledgement:** Still Hsu
