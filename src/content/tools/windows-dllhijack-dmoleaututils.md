---
trust_level: community
id: windows-dllhijack-dmoleaututils
namespace: windows:dllhijack:dmoleaututils
name: dmoleaututils.dll
description: "dmoleaututils.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmoleaututils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmoleaututils.html"
---
examples:
  - description: "Place malicious dmoleaututils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmoleaututils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\omadmclient.exe\""

# dmoleaututils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)

**Acknowledgement:** Wietze
