---
trust_level: community
id: windows-dllhijack-xolehlp
namespace: windows:dllhijack:xolehlp
name: xolehlp.dll
description: "xolehlp.dll — Sideloading hijacking (Microsoft)"
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
  template: "xolehlp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/xolehlp.html"
---
examples:
  - description: "Place malicious xolehlp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\xolehlp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msdtc.exe\""

# xolehlp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msdtc.exe (Sideloading)

**Acknowledgement:** Wietze
