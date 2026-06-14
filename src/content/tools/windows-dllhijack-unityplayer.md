---
trust_level: community
id: windows-dllhijack-unityplayer
namespace: windows:dllhijack:unityplayer
name: unityplayer.dll
description: "unityplayer.dll — Sideloading hijacking (Unity)"
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
  template: "unityplayer.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2023/05/03/doubled-dll-sideloading-dragon-breath/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/unityplayer.html"
---
examples:
  - description: "Place malicious unityplayer.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Temp\\%VERSION%\\Windows\\unityplayer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"KingdomTwoCrowns.exe\""

# unityplayer.dll

**Vendor:** Unity

**Expected Location:** %LOCALAPPDATA%\Temp\%VERSION%\Windows

**Vulnerable Executables:**
- KingdomTwoCrowns.exe (Sideloading)
