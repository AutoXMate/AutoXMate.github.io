---
trust_level: community
id: windows-dllhijack-authz
namespace: windows:dllhijack:authz
name: authz.dll
description: "authz.dll — Sideloading hijacking (Microsoft)"
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
  template: "authz.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/authz.html"
---
examples:
  - description: "Place malicious authz.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\authz.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\easinvoker.exe\""

# authz.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\easinvoker.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\whoami.exe (Sideloading)

**Acknowledgement:** Wietze
