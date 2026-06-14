---
trust_level: community
id: windows-dllhijack-tmdbglog
namespace: windows:dllhijack:tmdbglog
name: tmdbglog.dll
description: "tmdbglog.dll — Sideloading hijacking (Trend Micro)"
author: "Christiaan Beek"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "tmdbglog.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/space-pirates-tools-and-connections/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tmdbglog.html"
---
examples:
  - description: "Place malicious tmdbglog.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Trend Micro\\Titanium\\tmdbglog.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"PtWatchDog.exe\""

# tmdbglog.dll

**Vendor:** Trend Micro

**Expected Location:** %PROGRAMFILES%\Trend Micro\Titanium

**Vulnerable Executables:**
- PtWatchDog.exe (Sideloading)

**Acknowledgement:** Christiaan Beek

**Acknowledgement:** Claudio Teixeira
