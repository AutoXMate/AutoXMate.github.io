---
trust_level: community
id: windows-dllhijack-idstore
namespace: windows:dllhijack:idstore
name: idstore.dll
description: "idstore.dll — Environment Variable hijacking (Microsoft)"
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
  template: "idstore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/idstore.html"
---
examples:
  - description: "Place malicious idstore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\idstore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicecensus.exe\""

# idstore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicecensus.exe (Environment Variable)
- %SYSTEM32%\shellappruntime.exe (Environment Variable)

**Acknowledgement:** Wietze
