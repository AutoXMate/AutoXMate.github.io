---
trust_level: community
id: windows-dllhijack-connect
namespace: windows:dllhijack:connect
name: connect.dll
description: connect.dll — Environment Variable hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: connect.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/connect.html
features:
- network-intensive
- remote
---

examples:
  - description: "Place malicious connect.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\connect.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rasphone.exe\""

# connect.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
