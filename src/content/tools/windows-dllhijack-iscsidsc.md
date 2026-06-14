---
trust_level: community
id: windows-dllhijack-iscsidsc
namespace: windows:dllhijack:iscsidsc
name: iscsidsc.dll
description: "iscsidsc.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
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
  template: "iscsidsc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iscsidsc.html"
---
examples:
  - description: "Place malicious iscsidsc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iscsidsc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\iscsicli.exe\""

# iscsidsc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\iscsicli.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
