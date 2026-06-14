---
trust_level: community
id: windows-dllhijack-dmprocessxmlfiltered
namespace: windows:dllhijack:dmprocessxmlfiltered
name: dmprocessxmlfiltered.dll
description: "dmprocessxmlfiltered.dll — Sideloading hijacking (Microsoft)"
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
  template: "dmprocessxmlfiltered.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmprocessxmlfiltered.html"
---
examples:
  - description: "Place malicious dmprocessxmlfiltered.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmprocessxmlfiltered.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dmomacpmo.exe\""

# dmprocessxmlfiltered.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dmomacpmo.exe (Sideloading)

**Acknowledgement:** Wietze
