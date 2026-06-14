---
trust_level: community
id: windows-dllhijack-iscsiexe
namespace: windows:dllhijack:iscsiexe
name: iscsiexe.dll
description: "iscsiexe.dll — Search Order hijacking (Microsoft)"
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
  template: "iscsiexe.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC"
  - label: "Reference"
    url: "https://twitter.com/hackerfantastic/status/1547412574404214784"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iscsiexe.html"
---
examples:
  - description: "Place malicious iscsiexe.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iscsiexe.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\iscsicpl.exe\""

# iscsiexe.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\iscsicpl.exe (Search Order) [AutoElevate]

**Acknowledgement:** Matthew Hickey
