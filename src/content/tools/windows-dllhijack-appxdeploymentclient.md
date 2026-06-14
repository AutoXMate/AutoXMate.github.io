---
trust_level: community
id: windows-dllhijack-appxdeploymentclient
namespace: windows:dllhijack:appxdeploymentclient
name: appxdeploymentclient.dll
description: "appxdeploymentclient.dll — Sideloading hijacking (Microsoft)"
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
  template: "appxdeploymentclient.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/appxdeploymentclient.html"
---
examples:
  - description: "Place malicious appxdeploymentclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\appxdeploymentclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\lpremove.exe\""

# appxdeploymentclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\lpremove.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze
