---
trust_level: community
id: windows-dllhijack-msutb
namespace: windows:dllhijack:msutb
name: msutb.dll
description: "msutb.dll — Sideloading hijacking (Microsoft)"
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
  template: "msutb.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msutb.html"
---
examples:
  - description: "Place malicious msutb.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msutb.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ctfmon.exe\""

# msutb.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ctfmon.exe (Sideloading)

**Acknowledgement:** Wietze
