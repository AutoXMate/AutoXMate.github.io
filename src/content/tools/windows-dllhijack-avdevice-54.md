---
trust_level: community
id: windows-dllhijack-avdevice-54
namespace: windows:dllhijack:avdevice-54
name: avdevice-54.dll
description: "avdevice-54.dll — Sideloading hijacking (AnyMP4)"
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
  template: "avdevice-54.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/avdevice-54.html"
---
examples:
  - description: "Place malicious avdevice-54.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\AnyMP4 Studio\\AnyMP4 Blu-ray Creator\\avdevice-54.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\AnyMP4 Studio\\AnyMP4 Blu-ray Creator\\AnyMP4 Blu-ray Creator.exe\""

# avdevice-54.dll

**Vendor:** AnyMP4

**Expected Location:** %PROGRAMFILES%\AnyMP4 Studio\AnyMP4 Blu-ray Creator

**Vulnerable Executables:**
- %PROGRAMFILES%\AnyMP4 Studio\AnyMP4 Blu-ray Creator\AnyMP4 Blu-ray Creator.exe (Sideloading)

**Acknowledgement:** Chad Hudson

**Acknowledgement:** Jai Minton
