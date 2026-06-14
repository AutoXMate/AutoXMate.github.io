---
trust_level: community
id: windows-dllhijack-smadhook32c
namespace: windows:dllhijack:smadhook32c
name: smadhook32c.dll
description: "smadhook32c.dll — Sideloading hijacking (Smadav)"
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
  template: "smadhook32c.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/smadhook32c.html"
---
examples:
  - description: "Place malicious smadhook32c.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Smadav\\smadhook32c.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Smadav\\SmadHook.exe\""

# smadhook32c.dll

**Vendor:** Smadav

**Expected Location:** %PROGRAMFILES%\Smadav

**Vulnerable Executables:**
- %PROGRAMFILES%\Smadav\SmadHook.exe (Sideloading)
