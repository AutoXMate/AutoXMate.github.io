---
trust_level: community
id: windows-dllhijack-rjvplatform
namespace: windows:dllhijack:rjvplatform
name: rjvplatform.dll
description: "rjvplatform.dll — Sideloading hijacking (Microsoft)"
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
  template: "rjvplatform.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/0gtweet/status/1666716511988330499"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rjvplatform.html"
---
examples:
  - description: "Place malicious rjvplatform.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\SystemResetPlatform\\rjvplatform.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\SystemResetPlatform\\SystemResetPlatform.exe\""

# rjvplatform.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%\SystemResetPlatform

**Vulnerable Executables:**
- %SYSTEM32%\SystemResetPlatform\SystemResetPlatform.exe (Sideloading)

**Acknowledgement:** Grzegorz Tworek
