---
trust_level: community
id: windows-dllhijack-msxml3
namespace: windows:dllhijack:msxml3
name: msxml3.dll
description: "msxml3.dll — Environment Variable hijacking (Microsoft)"
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
  template: "msxml3.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msxml3.html"
---
examples:
  - description: "Place malicious msxml3.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msxml3.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wordpad.exe\""

# msxml3.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wordpad.exe (Environment Variable)

**Acknowledgement:** Wietze
