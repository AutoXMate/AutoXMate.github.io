---
trust_level: community
id: windows-dllhijack-libwsutil
namespace: windows:dllhijack:libwsutil
name: libwsutil.dll
description: "libwsutil.dll — Sideloading hijacking (Wireshark)"
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
  template: "libwsutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/fcb0272d586fff854ce9b329fbbba26902984a112a1afe96a149dbb2011ad289"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e91c4f990c1b0b58d69f3c3e80916463e5cc87011fd418d610c5264f7d5ecc9b"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libwsutil.html"
---
examples:
  - description: "Place malicious libwsutil.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Wireshark\\libwsutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Wireshark\\Mergecap.exe\""

# libwsutil.dll

**Vendor:** Wireshark

**Expected Location:** %PROGRAMFILES%\Wireshark

**Vulnerable Executables:**
- %PROGRAMFILES%\Wireshark\Mergecap.exe (Sideloading)

**Acknowledgement:** Jai Minton
