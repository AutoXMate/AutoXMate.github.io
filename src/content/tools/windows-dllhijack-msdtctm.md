---
trust_level: community
id: windows-dllhijack-msdtctm
namespace: windows:dllhijack:msdtctm
name: msdtctm.dll
description: "msdtctm.dll — Sideloading hijacking (Microsoft)"
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
  template: "msdtctm.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msdtctm.html"
---
examples:
  - description: "Place malicious msdtctm.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msdtctm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msdtc.exe\""

# msdtctm.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msdtc.exe (Sideloading)

**Acknowledgement:** Wietze
