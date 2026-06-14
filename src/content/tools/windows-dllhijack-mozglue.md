---
trust_level: community
id: windows-dllhijack-mozglue
namespace: windows:dllhijack:mozglue
name: mozglue.dll
description: "mozglue.dll — Sideloading hijacking (Mozilla)"
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
  template: "mozglue.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/SBousseaden/status/1530595156055011330"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mozglue.html"
---
examples:
  - description: "Place malicious mozglue.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\SeaMonkey\\mozglue.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\SeaMonkey\\seamonkey.exe\""

# mozglue.dll

**Vendor:** Mozilla

**Expected Location:** %PROGRAMFILES%\SeaMonkey

**Vulnerable Executables:**
- %PROGRAMFILES%\SeaMonkey\seamonkey.exe (Sideloading)

**Acknowledgement:** Samir
