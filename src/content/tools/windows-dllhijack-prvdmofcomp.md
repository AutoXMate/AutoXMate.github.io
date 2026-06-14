---
trust_level: community
id: windows-dllhijack-prvdmofcomp
namespace: windows:dllhijack:prvdmofcomp
name: prvdmofcomp.dll
description: "prvdmofcomp.dll — Sideloading hijacking (Microsoft)"
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
  template: "prvdmofcomp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/prvdmofcomp.html"
---
examples:
  - description: "Place malicious prvdmofcomp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\prvdmofcomp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\register-cimprovider.exe\""

# prvdmofcomp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\register-cimprovider.exe (Sideloading)

**Acknowledgement:** Wietze
