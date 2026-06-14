---
trust_level: community
id: windows-dllhijack-pla
namespace: windows:dllhijack:pla
name: pla.dll
description: "pla.dll — Environment Variable hijacking (Microsoft)"
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
  template: "pla.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/pla.html"
---
examples:
  - description: "Place malicious pla.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\pla.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\logman.exe\""

# pla.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\logman.exe (Environment Variable)

**Acknowledgement:** Wietze
