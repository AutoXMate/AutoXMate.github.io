---
trust_level: community
id: windows-dllhijack-mimetools
namespace: windows:dllhijack:mimetools
name: mimetools.dll
description: "mimetools.dll — Sideloading hijacking (Notepad++)"
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
  template: "mimetools.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/Cryptolaemus1/status/1770507063816241440"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mimetools.html"
---
examples:
  - description: "Place malicious mimetools.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Notepad++\\plugins\\mimetools.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Notepad++\\notepad++.exe\""

# mimetools.dll

**Vendor:** Notepad++

**Expected Location:** %PROGRAMFILES%\Notepad++\plugins

**Vulnerable Executables:**
- %PROGRAMFILES%\Notepad++\notepad++.exe (Sideloading)
