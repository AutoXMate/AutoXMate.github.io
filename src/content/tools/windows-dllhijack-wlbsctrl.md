---
trust_level: community
id: windows-dllhijack-wlbsctrl
namespace: windows:dllhijack:wlbsctrl
name: wlbsctrl.dll
description: "wlbsctrl.dll — Phantom hijacking (Microsoft)"
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
  template: "wlbsctrl.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://posts.specterops.io/lateral-movement-scm-and-dll-hijacking-primer-d2f61e8ab992"
  - label: "Reference"
    url: "https://www.youtube.com/watch?v=MZ8fgAN2As8"
  - label: "Reference"
    url: "https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wlbsctrl.html"
---
examples:
  - description: "Place malicious wlbsctrl.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wlbsctrl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\svchost.exe\""

# wlbsctrl.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\svchost.exe (Phantom)
