---
trust_level: community
id: windows-dllhijack-rasman
namespace: windows:dllhijack:rasman
name: rasman.dll
description: "rasman.dll — Sideloading hijacking (Microsoft)"
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
  template: "rasman.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rasman.html"
---
examples:
  - description: "Place malicious rasman.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\rasman.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cmdl32.exe\""

# rasman.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cmdl32.exe (Sideloading)
- %SYSTEM32%\nethost.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\rasautou.exe (Sideloading)
- %SYSTEM32%\rasdial.exe (Sideloading)

**Acknowledgement:** Wietze
