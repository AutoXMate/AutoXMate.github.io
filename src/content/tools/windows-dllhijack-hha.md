---
trust_level: community
id: windows-dllhijack-hha
namespace: windows:dllhijack:hha
name: hha.dll
description: "hha.dll — Sideloading hijacking (Microsoft)"
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
  template: "hha.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blog.trendmicro.com/trendlabs-security-intelligence/new-wave-of-plugx-targets-legitimate-apps/"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2016/03/10/beyond-good-ol-run-key-part-36/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/hha.html"
---
examples:
  - description: "Place malicious hha.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\hha.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\HTML Help Workshop\\hhc.exe\""

# hha.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\HTML Help Workshop\hhc.exe (Sideloading)

**Acknowledgement:** Adam
