---
trust_level: community
id: windows-dllhijack-qrt
namespace: windows:dllhijack:qrt
name: qrt.dll
description: "qrt.dll — Sideloading hijacking (F-Secure)"
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
  template: "qrt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.welivesecurity.com/2022/04/27/lookback-ta410-umbrella-cyberespionage-ttps-activity/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/qrt.html"
---
examples:
  - description: "Place malicious qrt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\F-Secure\\Anti-Virus\\qrt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"qrtfix.exe\""

# qrt.dll

**Vendor:** F-Secure

**Expected Location:** %PROGRAMFILES%\F-Secure\Anti-Virus

**Vulnerable Executables:**
- qrtfix.exe (Sideloading)
