---
trust_level: community
id: windows-dllhijack-mediainfo-i386
namespace: windows:dllhijack:mediainfo-i386
name: mediainfo_i386.dll
description: "mediainfo_i386.dll — Sideloading hijacking (MediaInfo)"
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
  template: "mediainfo_i386.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/69d9667cfab126f1c473163771511602497e05a908b3dbeaa29d165af879da97"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mediainfo-i386.html"
---
examples:
  - description: "Place malicious mediainfo_i386.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\MediaInfo\\mediainfo_i386.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\MediaInfo\\MediaInfo.exe\""

# mediainfo_i386.dll

**Vendor:** MediaInfo

**Expected Location:** %PROGRAMFILES%\MediaInfo

**Vulnerable Executables:**
- %PROGRAMFILES%\MediaInfo\MediaInfo.exe (Sideloading)

**Acknowledgement:** Michael Elford

**Acknowledgement:** Jai Minton
