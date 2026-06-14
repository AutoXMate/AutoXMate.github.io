---
trust_level: community
id: windows-dllhijack-dsclient
namespace: windows:dllhijack:dsclient
name: dsclient.dll
description: "dsclient.dll — Sideloading hijacking (Microsoft)"
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
  template: "dsclient.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dsclient.html"
---
examples:
  - description: "Place malicious dsclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dsclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dmcfghost.exe\""

# dsclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dmcfghost.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\dstokenclean.exe (Sideloading)

**Acknowledgement:** Wietze
