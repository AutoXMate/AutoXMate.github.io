---
trust_level: community
id: windows-dllhijack-dhcpcsvc
namespace: windows:dllhijack:dhcpcsvc
name: dhcpcsvc.dll
description: dhcpcsvc.dll — Sideloading hijacking (Microsoft)
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
  template: dhcpcsvc.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/dhcpcsvc.html
features:
- file-system
---

examples:
  - description: "Place malicious dhcpcsvc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dhcpcsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ipconfig.exe\""

# dhcpcsvc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ipconfig.exe (Sideloading)
- %SYSTEM32%\netiougc.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
