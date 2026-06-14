---
trust_level: community
id: windows-dllhijack-loadperf
namespace: windows:dllhijack:loadperf
name: loadperf.dll
description: "loadperf.dll — Sideloading hijacking (Microsoft)"
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
  template: "loadperf.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/loadperf.html"
---
examples:
  - description: "Place malicious loadperf.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\loadperf.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\unlodctr.exe\""

# loadperf.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\unlodctr.exe (Sideloading)

**Acknowledgement:** Wietze
