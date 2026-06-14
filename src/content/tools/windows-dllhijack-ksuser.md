---
trust_level: community
id: windows-dllhijack-ksuser
namespace: windows:dllhijack:ksuser
name: ksuser.dll
description: "ksuser.dll — Sideloading hijacking (Microsoft)"
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
  template: "ksuser.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ksuser.html"
---
examples:
  - description: "Place malicious ksuser.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ksuser.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mfpmp.exe\""

# ksuser.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mfpmp.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)

**Acknowledgement:** Wietze
