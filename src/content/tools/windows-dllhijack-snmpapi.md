---
trust_level: community
id: windows-dllhijack-snmpapi
namespace: windows:dllhijack:snmpapi
name: snmpapi.dll
description: "snmpapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "snmpapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/snmpapi.html"
---
examples:
  - description: "Place malicious snmpapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\snmpapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\arp.exe\""

# snmpapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\arp.exe (Sideloading)
- %SYSTEM32%\netstat.exe (Sideloading)

**Acknowledgement:** Wietze
