---
trust_level: community
id: windows-dllhijack-mstracer
namespace: windows:dllhijack:mstracer
name: mstracer.dll
description: "mstracer.dll — Phantom hijacking (Microsoft)"
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
  template: "mstracer.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2015/02/23/beyond-good-ol-run-key-part-28/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mstracer.html"
---
examples:
  - description: "Place malicious mstracer.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mstracer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\searchindexer.exe\""

# mstracer.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\searchindexer.exe (Phantom)
- %SYSTEM32%\searchprotocolhost.exe (Phantom)

**Acknowledgement:** Adam
