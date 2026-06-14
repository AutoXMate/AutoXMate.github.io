---
trust_level: community
id: windows-dllhijack-fhcfg
namespace: windows:dllhijack:fhcfg
name: fhcfg.dll
description: "fhcfg.dll — Environment Variable hijacking (Microsoft)"
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
  template: "fhcfg.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fhcfg.html"
---
examples:
  - description: "Place malicious fhcfg.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fhcfg.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\filehistory.exe\""

# fhcfg.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\filehistory.exe (Environment Variable)

**Acknowledgement:** Wietze
