---
trust_level: community
id: windows-dllhijack-fddevquery
namespace: windows:dllhijack:fddevquery
name: fddevquery.dll
description: "fddevquery.dll — Environment Variable hijacking (Microsoft)"
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
  template: "fddevquery.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fddevquery.html"
---
examples:
  - description: "Place malicious fddevquery.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fddevquery.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ddodiag.exe\""

# fddevquery.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ddodiag.exe (Environment Variable)

**Acknowledgement:** Wietze
