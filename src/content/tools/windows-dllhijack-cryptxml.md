---
trust_level: community
id: windows-dllhijack-cryptxml
namespace: windows:dllhijack:cryptxml
name: cryptxml.dll
description: "cryptxml.dll — Sideloading hijacking (Microsoft)"
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
  template: "cryptxml.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cryptxml.html"
---
examples:
  - description: "Place malicious cryptxml.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cryptxml.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\clipup.exe\""

# cryptxml.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\clipup.exe (Sideloading)
- %SYSTEM32%\sppsvc.exe (Sideloading)

**Acknowledgement:** Wietze
