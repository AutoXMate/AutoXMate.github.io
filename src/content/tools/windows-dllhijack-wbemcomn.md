---
trust_level: community
id: windows-dllhijack-wbemcomn
namespace: windows:dllhijack:wbemcomn
name: wbemcomn.dll
description: "wbemcomn.dll — Search Order hijacking (Microsoft)"
author: "v1stra"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wbemcomn.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://gist.github.com/v1stra/7a13f2a27a1c9b97778d12e13a3d53c2"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wbemcomn.html"
---
examples:
  - description: "Place malicious wbemcomn.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wbemcomn.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\Wbem\\WmiApSrv.exe\""

# wbemcomn.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\Wbem\WmiApSrv.exe (Search Order)

**Acknowledgement:** v1stra
