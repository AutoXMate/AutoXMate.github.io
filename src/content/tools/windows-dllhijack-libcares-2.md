---
trust_level: community
id: windows-dllhijack-libcares-2
namespace: windows:dllhijack:libcares-2
name: libcares-2.dll
description: "libcares-2.dll — Sideloading hijacking (c-ares)"
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
  template: "libcares-2.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trellix.com/en-us/blogs/research/hiding-in-plain-sight-multi-actor-ahost-exe-attacks/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/7c41ac7b5bf15e34d50d6abbe28254e94e6c21e0ccab9fa68aca05049a515758"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libcares-2.html"
---
examples:
  - description: "Place malicious libcares-2.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\GitKraken\\app-%VERSION%\\libcares-2.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"ahost.exe\""

# libcares-2.dll

**Vendor:** c-ares

**Expected Location:** %LOCALAPPDATA%\GitKraken\app-%VERSION%

**Vulnerable Executables:**
- ahost.exe (Sideloading)
