---
trust_level: community
id: windows-dllhijack-ssshim
namespace: windows:dllhijack:ssshim
name: ssshim.dll
description: ssshim.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
- security.privilegeescalation.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
- privilege-escalation
execution:
  template: ssshim.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://twitter.com/0gtweet/status/1363107343018385410
- label: HijackLibs
  url: https://hijacklibs.net/entries/ssshim.html
features:
- network-intensive
- requires-root
---

examples:
  - description: "Place malicious ssshim.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ssshim.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\sfc.exe\""

# ssshim.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\sfc.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Grzegorz Tworek
