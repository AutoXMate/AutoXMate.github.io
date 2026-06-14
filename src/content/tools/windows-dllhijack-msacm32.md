---
trust_level: community
id: windows-dllhijack-msacm32
namespace: windows:dllhijack:msacm32
name: msacm32.dll
description: "msacm32.dll — Sideloading hijacking (Microsoft)"
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
  template: "msacm32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msacm32.html"
---
examples:
  - description: "Place malicious msacm32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msacm32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\osk.exe\""

# msacm32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\osk.exe (Sideloading)

**Acknowledgement:** Wietze
