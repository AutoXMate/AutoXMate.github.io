---
trust_level: community
id: windows-dllhijack-launcher
namespace: windows:dllhijack:launcher
name: launcher.dll
description: "launcher.dll — Search Order hijacking (Oracle)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "launcher.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/c3b48c62b34510e2328b790f9fabed994a91998f36c0c40bcf628b93f40d8ae5/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/launcher.html"
---
examples:
  - description: "Place malicious launcher.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\SQL Developer\\ide\\bin\\launcher.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\SQL Developer\\sqldeveloper.exe\""

# launcher.dll

**Vendor:** Oracle

**Expected Location:** %PROGRAMFILES%\SQL Developer\ide\bin

**Vulnerable Executables:**
- %PROGRAMFILES%\SQL Developer\sqldeveloper.exe (Search Order)

**Acknowledgement:** Jai Minton
