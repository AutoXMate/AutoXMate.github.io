---
trust_level: community
id: windows-dllhijack-tosbtkbd
namespace: windows:dllhijack:tosbtkbd
name: tosbtkbd.dll
description: "tosbtkbd.dll — Sideloading hijacking (Toshiba)"
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
  template: "tosbtkbd.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://vms.drweb.com/virus/?i=21995048"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tosbtkbd.html"
---
examples:
  - description: "Place malicious tosbtkbd.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Toshiba\\Bluetooth Toshiba Stack\\tosbtkbd.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Toshiba\\Bluetooth Toshiba Stack\\TosBtKbd.exe\""

# tosbtkbd.dll

**Vendor:** Toshiba

**Expected Location:** %PROGRAMFILES%\Toshiba\Bluetooth Toshiba Stack

**Vulnerable Executables:**
- %PROGRAMFILES%\Toshiba\Bluetooth Toshiba Stack\TosBtKbd.exe (Sideloading)
