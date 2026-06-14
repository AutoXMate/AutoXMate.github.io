---
trust_level: community
id: windows-dllhijack-msftedit
namespace: windows:dllhijack:msftedit
name: msftedit.dll
description: "msftedit.dll — Phantom, Sideloading hijacking (Microsoft)"
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
  template: "msftedit.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2015/02/23/beyond-good-ol-run-key-part-28/"
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msftedit.html"
---
examples:
  - description: "Place malicious msftedit.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msftedit.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\charmap.exe\""

# msftedit.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\charmap.exe (Sideloading)
- %SYSTEM32%\mspaint.exe (Sideloading)
- %SYSTEM32%\searchindexer.exe (Phantom)
- %SYSTEM32%\searchprotocolhost.exe (Phantom)

**Acknowledgement:** Adam

**Acknowledgement:** Wietze
