---
trust_level: community
id: windows-dllhijack-safestore32
namespace: windows:dllhijack:safestore32
name: safestore32.dll
description: "safestore32.dll — Sideloading hijacking (Sophos)"
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
  template: "safestore32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://symantec.broadcom.com/hubfs/Attacks-Against-Government-Sector.pdf"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/safestore32.html"
---
examples:
  - description: "Place malicious safestore32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Sophos\\Sophos Anti-Virus\\safestore32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Sophos\\Sophos Anti-Virus\\ssr32.exe\""

# safestore32.dll

**Vendor:** Sophos

**Expected Location:** %PROGRAMFILES%\Sophos\Sophos Anti-Virus

**Vulnerable Executables:**
- %PROGRAMFILES%\Sophos\Sophos Anti-Virus\ssr32.exe (Sideloading)
