---
trust_level: community
id: windows-dllhijack-libglib-2-0-0
namespace: windows:dllhijack:libglib-2-0-0
name: libglib-2.0-0.dll
description: "libglib-2.0-0.dll — Sideloading hijacking (Wireshark)"
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
  template: "libglib-2.0-0.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/fcb0272d586fff854ce9b329fbbba26902984a112a1afe96a149dbb2011ad289"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libglib-2-0-0.html"
---
examples:
  - description: "Place malicious libglib-2.0-0.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Wireshark\\libglib-2.0-0.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Wireshark\\Mergecap.exe\""

# libglib-2.0-0.dll

**Vendor:** Wireshark

**Expected Location:** %PROGRAMFILES%\Wireshark

**Vulnerable Executables:**
- %PROGRAMFILES%\Wireshark\Mergecap.exe (Sideloading)

**Acknowledgement:** Jai Minton
