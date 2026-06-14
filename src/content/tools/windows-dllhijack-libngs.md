---
trust_level: community
id: windows-dllhijack-libngs
namespace: windows:dllhijack:libngs
name: libngs.dll
description: "libngs.dll — Sideloading hijacking (Sangfor)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "libngs.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securelist.com/honeymyte-updates-coolclient-uses-browser-stealers-and-scripts/118664/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libngs.html"
---
examples:
  - description: "Place malicious libngs.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Sangfor\\SSL\\RemoteAppClient\\\\libngs.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Sangfor\\SSL\\RemoteAppClient\\SRAPSession.exe\""

# libngs.dll

**Vendor:** Sangfor

**Expected Location:** %PROGRAMFILES%\Sangfor\SSL\RemoteAppClient\

**Vulnerable Executables:**
- %PROGRAMFILES%\Sangfor\SSL\RemoteAppClient\SRAPSession.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
