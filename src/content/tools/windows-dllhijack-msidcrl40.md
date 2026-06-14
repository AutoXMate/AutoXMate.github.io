---
trust_level: community
id: windows-dllhijack-msidcrl40
namespace: windows:dllhijack:msidcrl40
name: msidcrl40.dll
description: "msidcrl40.dll — Sideloading hijacking (Microsoft)"
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
  template: "msidcrl40.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e2787ddbbf2a7304827a17d698f7cede17edbf0633d36f39f4c020ee8f37ccd1"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/448bfca5913e45ec36863ec2e72d959bd1f8ac30e0c794b708b3a6f45a050ef4"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msidcrl40.html"
---
examples:
  - description: "Place malicious msidcrl40.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\msn messenger\\msidcrl40.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\msn messenger\\livecall.exe\""

# msidcrl40.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\msn messenger

**Vulnerable Executables:**
- %PROGRAMFILES%\msn messenger\livecall.exe (Sideloading)

**Acknowledgement:** Jai Minton
