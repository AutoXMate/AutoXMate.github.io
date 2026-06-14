---
trust_level: community
id: windows-dllhijack-libcurl
namespace: windows:dllhijack:libcurl
name: libcurl.dll
description: "libcurl.dll — Sideloading hijacking (curl)"
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
  template: "libcurl.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d1e44e4224899cb160a92f4c7f4f042b10ae0ee3fc16bbe457ad32e8b1527ed5"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/dd0c2d79fef0cf5e2d32dcdd661d6ba0a6e9901ffe047fad2d081bbc28daad2c"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libcurl.html"
---
examples:
  - description: "Place malicious libcurl.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Notepad++\\updater\\libcurl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Notepad++\\updater\\GUP.exe\""

# libcurl.dll

**Vendor:** curl

**Expected Location:** %PROGRAMFILES%\Notepad++\updater

**Vulnerable Executables:**
- %PROGRAMFILES%\Notepad++\updater\GUP.exe (Sideloading)
- %PROGRAMFILES%\Coolmuster\Coolmuster PDF Creator Pro\%VERSION%\Bin\Coolmuster PDF Creator Pro.exe (Sideloading)

**Acknowledgement:** Still Hsu

**Acknowledgement:** Jai Minton
