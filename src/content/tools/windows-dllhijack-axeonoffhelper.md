---
trust_level: community
id: windows-dllhijack-axeonoffhelper
namespace: windows:dllhijack:axeonoffhelper
name: axeonoffhelper.dll
description: "axeonoffhelper.dll — Phantom hijacking (Microsoft)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "axeonoffhelper.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/axeonoffhelper.html"
---
examples:
  - description: "Place malicious axeonoffhelper.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\axeonoffhelper.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wpr.exe\""

# axeonoffhelper.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\wpr.exe (Phantom)

**Acknowledgement:** Adam

**Acknowledgement:** Swachchhanda Shrawan Poudel
