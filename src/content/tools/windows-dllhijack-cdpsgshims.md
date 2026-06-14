---
trust_level: community
id: windows-dllhijack-cdpsgshims
namespace: windows:dllhijack:cdpsgshims
name: cdpsgshims.dll
description: "cdpsgshims.dll — Phantom hijacking (Microsoft)"
author: "k4nfr3"
version: "1.0.0"
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
  template: "cdpsgshims.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://itm4n.github.io/cdpsvc-dll-hijacking/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cdpsgshims.html"
---
examples:
  - description: "Place malicious cdpsgshims.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cdpsgshims.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\svchost.exe\""

# cdpsgshims.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\svchost.exe (Phantom) [PrivEsc]

**Acknowledgement:** itm4n
