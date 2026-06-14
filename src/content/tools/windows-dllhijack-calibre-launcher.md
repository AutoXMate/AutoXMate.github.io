---
trust_level: community
id: windows-dllhijack-calibre-launcher
namespace: windows:dllhijack:calibre-launcher
name: calibre-launcher.dll
description: "calibre-launcher.dll — Sideloading hijacking (Calibre)"
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
  template: "calibre-launcher.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.huntress.com/blog/advanced-persistent-threat-targeting-vietnamese-human-rights-defenders"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/calibre-launcher.html"
---
examples:
  - description: "Place malicious calibre-launcher.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Calibre2\\calibre-launcher.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"calibre.exe\""

# calibre-launcher.dll

**Vendor:** Calibre

**Expected Location:** %PROGRAMFILES%\Calibre2

**Vulnerable Executables:**
- calibre.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Craig Sweeney
