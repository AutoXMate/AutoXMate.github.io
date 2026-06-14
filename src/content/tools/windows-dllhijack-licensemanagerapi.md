---
trust_level: community
id: windows-dllhijack-licensemanagerapi
namespace: windows:dllhijack:licensemanagerapi
name: licensemanagerapi.dll
description: licensemanagerapi.dll — Sideloading hijacking (Microsoft)
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
  template: licensemanagerapi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/licensemanagerapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious licensemanagerapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\licensemanagerapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wsreset.exe\""

# licensemanagerapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wsreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
