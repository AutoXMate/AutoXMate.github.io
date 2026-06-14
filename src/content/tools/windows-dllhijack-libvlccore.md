---
trust_level: community
id: windows-dllhijack-libvlccore
namespace: windows:dllhijack:libvlccore
name: libvlccore.dll
description: "libvlccore.dll — Sideloading hijacking (VLC)"
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
  template: "libvlccore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/33c08eeaff6e9aa686a14144cb84d1895f260d28b767a0d2a10dbe427a65d7c0"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libvlccore.html"
---
examples:
  - description: "Place malicious libvlccore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VideoLAN\\VLC\\libvlccore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\VideoLAN\\VLC\\vlc.exe\""

# libvlccore.dll

**Vendor:** VLC

**Expected Location:** %PROGRAMFILES%\VideoLAN\VLC

**Vulnerable Executables:**
- %PROGRAMFILES%\VideoLAN\VLC\vlc.exe (Sideloading)

**Acknowledgement:** Jai Minton
