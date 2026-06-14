---
trust_level: community
id: windows-dllhijack-miutils
namespace: windows:dllhijack:miutils
name: miutils.dll
description: "miutils.dll — Sideloading hijacking (Microsoft)"
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
  template: "miutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/miutils.html"
---
examples:
  - description: "Place malicious miutils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\miutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\register-cimprovider.exe\""

# miutils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\register-cimprovider.exe (Sideloading)
- %SYSTEM32%\winrs.exe (Sideloading)
- %SYSTEM32%\wsmanhttpconfig.exe (Sideloading)
- %SYSTEM32%\wsmprovhost.exe (Sideloading)

**Acknowledgement:** Wietze
