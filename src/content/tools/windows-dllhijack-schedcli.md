---
trust_level: community
id: windows-dllhijack-schedcli
namespace: windows:dllhijack:schedcli
name: schedcli.dll
description: "schedcli.dll — Sideloading hijacking (Microsoft)"
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
  template: "schedcli.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/schedcli.html"
---
examples:
  - description: "Place malicious schedcli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\schedcli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\at.exe\""

# schedcli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\at.exe (Sideloading)

**Acknowledgement:** Wietze
