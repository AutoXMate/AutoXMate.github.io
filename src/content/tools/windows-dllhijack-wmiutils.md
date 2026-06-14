---
trust_level: community
id: windows-dllhijack-wmiutils
namespace: windows:dllhijack:wmiutils
name: wmiutils.dll
description: "wmiutils.dll — Environment Variable hijacking (Microsoft)"
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
  template: "wmiutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wmiutils.html"
---
examples:
  - description: "Place malicious wmiutils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wbem\\wmiutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\stordiag.exe\""

# wmiutils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%\wbem

**Vulnerable Executables:**
- %SYSTEM32%\stordiag.exe (Environment Variable)
- %SYSTEM32%\tasklist.exe (Environment Variable)

**Acknowledgement:** Wietze
