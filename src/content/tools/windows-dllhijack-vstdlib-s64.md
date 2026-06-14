---
trust_level: community
id: windows-dllhijack-vstdlib-s64
namespace: windows:dllhijack:vstdlib-s64
name: vstdlib_s64.dll
description: "vstdlib_s64.dll — Sideloading hijacking (Valve)"
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
  template: "vstdlib_s64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-09-19-IOCs-for-file-downloader-to-Lumma-Stealer.txt"
  - label: "Reference"
    url: "https://twitter.com/Unit42_Intel/status/1837137726409158770"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vstdlib-s64.html"
---
examples:
  - description: "Place malicious vstdlib_s64.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Steam\\vstdlib_s64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Steam\\steamerrorreporter64.exe\""

# vstdlib_s64.dll

**Vendor:** Valve

**Expected Location:** %PROGRAMFILES%\Steam

**Vulnerable Executables:**
- %PROGRAMFILES%\Steam\steamerrorreporter64.exe (Sideloading)

**Acknowledgement:** Unit 42
