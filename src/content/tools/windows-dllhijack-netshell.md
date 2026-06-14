---
trust_level: community
id: windows-dllhijack-netshell
namespace: windows:dllhijack:netshell
name: netshell.dll
description: netshell.dll — Sideloading, Environment Variable hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: netshell.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/netshell.html
features:
- interactive
---

examples:
  - description: "Place malicious netshell.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\netshell.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# netshell.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
