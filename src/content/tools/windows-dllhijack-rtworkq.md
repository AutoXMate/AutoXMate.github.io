---
trust_level: community
id: windows-dllhijack-rtworkq
namespace: windows:dllhijack:rtworkq
name: rtworkq.dll
description: "rtworkq.dll — Sideloading hijacking (Microsoft)"
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
  template: "rtworkq.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rtworkq.html"
---
examples:
  - description: "Place malicious rtworkq.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\rtworkq.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mdeserver.exe\""

# rtworkq.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mdeserver.exe (Sideloading)
- %SYSTEM32%\mfpmp.exe (Sideloading)

**Acknowledgement:** Wietze
