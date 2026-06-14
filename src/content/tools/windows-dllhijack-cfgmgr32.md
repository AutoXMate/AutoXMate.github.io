---
trust_level: community
id: windows-dllhijack-cfgmgr32
namespace: windows:dllhijack:cfgmgr32
name: cfgmgr32.dll
description: "cfgmgr32.dll — Sideloading hijacking (Microsoft)"
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
  template: "cfgmgr32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cfgmgr32.html"
---
examples:
  - description: "Place malicious cfgmgr32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cfgmgr32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\write.exe\""

# cfgmgr32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Wietze
