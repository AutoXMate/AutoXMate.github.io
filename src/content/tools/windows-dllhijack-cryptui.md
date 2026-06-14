---
trust_level: community
id: windows-dllhijack-cryptui
namespace: windows:dllhijack:cryptui
name: cryptui.dll
description: "cryptui.dll — Sideloading hijacking (Microsoft)"
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
  template: "cryptui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cryptui.html"
---
examples:
  - description: "Place malicious cryptui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cryptui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certutil.exe\""

# cryptui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)

**Acknowledgement:** Wietze
