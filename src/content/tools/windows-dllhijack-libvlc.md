---
trust_level: community
id: windows-dllhijack-libvlc
namespace: windows:dllhijack:libvlc
name: libvlc.dll
description: "libvlc.dll — Sideloading hijacking (VLC)"
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
  template: "libvlc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2022/11/03/family-tree-dll-sideloading-cases-may-be-related/"
  - label: "Reference"
    url: "https://www.microsoft.com/en-us/security/blog/2018/11/08/attack-uses-malicious-inpage-document-and-outdated-vlc-media-player-to-give-attackers-backdoor-access-to-targets/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libvlc.html"
---
examples:
  - description: "Place malicious libvlc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VideoLAN\\VLC\\libvlc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\VideoLAN\\VLC\\vlc.exe\""

# libvlc.dll

**Vendor:** VLC

**Expected Location:** %PROGRAMFILES%\VideoLAN\VLC

**Vulnerable Executables:**
- %PROGRAMFILES%\VideoLAN\VLC\vlc.exe (Sideloading)
