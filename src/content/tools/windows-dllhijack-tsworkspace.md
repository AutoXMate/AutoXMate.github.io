---
trust_level: community
id: windows-dllhijack-tsworkspace
namespace: windows:dllhijack:tsworkspace
name: tsworkspace.dll
description: "tsworkspace.dll — Sideloading hijacking (Microsoft)"
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
  template: "tsworkspace.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tsworkspace.html"
---
examples:
  - description: "Place malicious tsworkspace.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tsworkspace.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wkspbroker.exe\""

# tsworkspace.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wkspbroker.exe (Sideloading)

**Acknowledgement:** Wietze
