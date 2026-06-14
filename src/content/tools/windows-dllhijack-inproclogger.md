---
trust_level: community
id: windows-dllhijack-inproclogger
namespace: windows:dllhijack:inproclogger
name: inproclogger.dll
description: "inproclogger.dll — Sideloading hijacking (Microsoft)"
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
  template: "inproclogger.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/inproclogger.html"
---
examples:
  - description: "Place malicious inproclogger.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\inproclogger.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\easpolicymanagerbrokerhost.exe\""

# inproclogger.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\easpolicymanagerbrokerhost.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
