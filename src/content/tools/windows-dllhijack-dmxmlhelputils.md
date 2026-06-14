---
trust_level: community
id: windows-dllhijack-dmxmlhelputils
namespace: windows:dllhijack:dmxmlhelputils
name: dmxmlhelputils.dll
description: "dmxmlhelputils.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmxmlhelputils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmxmlhelputils.html"
---
examples:
  - description: "Place malicious dmxmlhelputils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmxmlhelputils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dmcfghost.exe\""

# dmxmlhelputils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dmcfghost.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)

**Acknowledgement:** Wietze
