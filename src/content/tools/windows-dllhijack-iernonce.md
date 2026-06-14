---
trust_level: community
id: windows-dllhijack-iernonce
namespace: windows:dllhijack:iernonce
name: iernonce.dll
description: "iernonce.dll — Sideloading hijacking (Microsoft)"
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
  template: "iernonce.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/12/26/1-little-known-secret-of-runonce-exe-32-bit/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iernonce.html"
---
examples:
  - description: "Place malicious iernonce.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iernonce.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSWOW64%\\runonce.exe\""

# iernonce.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSWOW64%\runonce.exe (Sideloading)

**Acknowledgement:** Adam
