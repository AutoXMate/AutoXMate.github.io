---
trust_level: community
id: windows-dllhijack-nlansp-c
namespace: windows:dllhijack:nlansp-c
name: nlansp_c.dll
description: "nlansp_c.dll — Environment Variable hijacking (Microsoft)"
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
  template: "nlansp_c.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/nlansp-c.html"
---
examples:
  - description: "Place malicious nlansp_c.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\nlansp_c.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ftp.exe\""

# nlansp_c.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ftp.exe (Environment Variable)
- %SYSTEM32%\hostname.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)

**Acknowledgement:** Wietze
