---
trust_level: community
id: windows-dllhijack-wow64log
namespace: windows:dllhijack:wow64log
name: wow64log.dll
description: "wow64log.dll — Phantom hijacking (Microsoft)"
author: "ice-wzl"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wow64log.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://waleedassar.blogspot.com/2013/01/wow64logdll.html"
  - label: "Reference"
    url: "https://github.com/ice-wzl/Cmder_DLL_Side-Loading/blob/main/README.md"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wow64log.html"
---
examples:
  - description: "Place malicious wow64log.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wow64log.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"cmder.exe\""

# wow64log.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- cmder.exe (Phantom)

**Acknowledgement:** ice-wzl
