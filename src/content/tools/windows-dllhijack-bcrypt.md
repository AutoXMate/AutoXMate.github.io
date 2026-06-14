---
trust_level: community
id: windows-dllhijack-bcrypt
namespace: windows:dllhijack:bcrypt
name: bcrypt.dll
description: "bcrypt.dll — Environment Variable hijacking (Microsoft)"
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
  template: "bcrypt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bcrypt.html"
---
examples:
  - description: "Place malicious bcrypt.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bcrypt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\shellappruntime.exe\""

# bcrypt.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\shellappruntime.exe (Environment Variable)
- %SYSTEM32%\wordpad.exe (Environment Variable)

**Acknowledgement:** Wietze
