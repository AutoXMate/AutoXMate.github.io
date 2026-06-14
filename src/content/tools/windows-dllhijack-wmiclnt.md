---
trust_level: community
id: windows-dllhijack-wmiclnt
namespace: windows:dllhijack:wmiclnt
name: wmiclnt.dll
description: wmiclnt.dll — Sideloading hijacking (Microsoft)
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
  template: wmiclnt.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/wmiclnt.html
features:
- requires-root
---

examples:
  - description: "Place malicious wmiclnt.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wmiclnt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dispdiag.exe\""

# wmiclnt.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dispdiag.exe (Sideloading)
- %SYSTEM32%\iscsicli.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
