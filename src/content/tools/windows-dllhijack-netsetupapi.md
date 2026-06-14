---
trust_level: community
id: windows-dllhijack-netsetupapi
namespace: windows:dllhijack:netsetupapi
name: netsetupapi.dll
description: "netsetupapi.dll — Environment Variable hijacking (Microsoft)"
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
  template: "netsetupapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/netsetupapi.html"
---
examples:
  - description: "Place malicious netsetupapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\netsetupapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rasphone.exe\""

# netsetupapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
