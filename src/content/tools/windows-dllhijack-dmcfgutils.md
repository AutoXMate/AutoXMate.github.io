---
trust_level: community
id: windows-dllhijack-dmcfgutils
namespace: windows:dllhijack:dmcfgutils
name: dmcfgutils.dll
description: "dmcfgutils.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmcfgutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmcfgutils.html"
---
examples:
  - description: "Place malicious dmcfgutils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmcfgutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\omadmclient.exe\""

# dmcfgutils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\omadmclient.exe (Sideloading)

**Acknowledgement:** Wietze
