---
trust_level: community
id: windows-dllhijack-mfplat
namespace: windows:dllhijack:mfplat
name: mfplat.dll
description: "mfplat.dll — Sideloading hijacking (Microsoft)"
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
  template: "mfplat.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mfplat.html"
---
examples:
  - description: "Place malicious mfplat.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mfplat.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mdeserver.exe\""

# mfplat.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mdeserver.exe (Sideloading)
- %SYSTEM32%\mfpmp.exe (Sideloading)

**Acknowledgement:** Wietze
