---
trust_level: community
id: windows-dllhijack-register
namespace: windows:dllhijack:register
name: register.dll
description: "register.dll — Sideloading hijacking (IObit)"
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
  template: "register.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/0500e5ad7e344d32ee26da988aeb30f6344a0c89a68eacce5d6a5683d1fee0e1/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/cdfe0f80cd3dc1914c7ad1a6305c0c1116168a37c5cfe8ff51650e2ac814b818/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/register.html"
---
examples:
  - description: "Place malicious register.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\IObit\\Driver Booster\\%VERSION%\\register.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\IObit\\Driver Booster\\%VERSION%\\DriverBooster.exe\""

# register.dll

**Vendor:** IObit

**Expected Location:** %PROGRAMFILES%\IObit\Driver Booster\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\IObit\Driver Booster\%VERSION%\DriverBooster.exe (Sideloading)

**Acknowledgement:** Jai Minton
