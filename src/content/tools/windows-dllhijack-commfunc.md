---
trust_level: community
id: windows-dllhijack-commfunc
namespace: windows:dllhijack:commfunc
name: commfunc.dll
description: "commfunc.dll — Sideloading hijacking (Lenovo)"
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
  template: "commfunc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blog.trendmicro.com/trendlabs-security-intelligence/new-wave-of-plugx-targets-legitimate-apps/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/commfunc.html"
---
examples:
  - description: "Place malicious commfunc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Lenovo\\Communications Utility\\commfunc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"cammute.exe\""

# commfunc.dll

**Vendor:** Lenovo

**Expected Location:** %PROGRAMFILES%\Lenovo\Communications Utility

**Vulnerable Executables:**
- cammute.exe (Sideloading)
