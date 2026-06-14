---
trust_level: community
id: windows-dllhijack-dhcpcmonitor
namespace: windows:dllhijack:dhcpcmonitor
name: dhcpcmonitor.dll
description: dhcpcmonitor.dll — Sideloading hijacking (Microsoft)
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
  template: dhcpcmonitor.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/dhcpcmonitor.html
features:
- file-system
- streaming
---

examples:
  - description: "Place malicious dhcpcmonitor.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dhcpcmonitor.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# dhcpcmonitor.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze
