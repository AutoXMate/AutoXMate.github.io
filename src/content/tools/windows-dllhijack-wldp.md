---
trust_level: community
id: windows-dllhijack-wldp
namespace: windows:dllhijack:wldp
name: wldp.dll
description: wldp.dll — Sideloading hijacking (Microsoft)
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
  template: wldp.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/wldp.html
features:
- requires-root
---

examples:
  - description: "Place malicious wldp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wldp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mshta.exe\""

# wldp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\write.exe (Sideloading)

**Acknowledgement:** Wietze
