---
trust_level: community
id: windows-dllhijack-mintdh
namespace: windows:dllhijack:mintdh
name: mintdh.dll
description: "mintdh.dll — Sideloading hijacking (Microsoft)"
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
  template: "mintdh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mintdh.html"
---
examples:
  - description: "Place malicious mintdh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mintdh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\applytrustoffline.exe\""

# mintdh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\applytrustoffline.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\pktmon.exe (Sideloading)
- %SYSTEM32%\plasrv.exe (Sideloading)

**Acknowledgement:** Wietze
