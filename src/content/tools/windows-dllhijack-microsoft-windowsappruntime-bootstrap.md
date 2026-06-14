---
trust_level: community
id: windows-dllhijack-microsoft-windowsappruntime-bootstrap
namespace: windows:dllhijack:microsoft-windowsappruntime-bootstrap
name: microsoft.windowsappruntime.bootstrap.dll
description: microsoft.windowsappruntime.bootstrap.dll — Sideloading hijacking (Microsoft)
author: Swachchhanda Shrawan Poudel
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: microsoft.windowsappruntime.bootstrap.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.acronis.com/en/tru/posts/same-packet-different-magic-mustang-panda-hits-indias-banking-sector-and-korea-geopolitics/
- label: Reference
  url: https://www.virustotal.com/gui/file/6cd52ea299e99e3cf4a175b83a35b5a2516ce44a2c3c43b9d7a152753258998c
- label: HijackLibs
  url: https://hijacklibs.net/entries/microsoft-windowsappruntime-bootstrap.html
features:
- process-manip
---

examples:
  - description: "Place malicious microsoft.windowsappruntime.bootstrap.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\microsoft.windowsappruntime.bootstrap.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"kwpswnsserver.exe\""

# microsoft.windowsappruntime.bootstrap.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- kwpswnsserver.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
