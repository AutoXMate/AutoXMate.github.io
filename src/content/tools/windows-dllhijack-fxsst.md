---
trust_level: community
id: windows-dllhijack-fxsst
namespace: windows:dllhijack:fxsst
name: fxsst.dll
description: "fxsst.dll — Search Order hijacking (Microsoft)"
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
  template: "fxsst.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.fireeye.com/blog/threat-research/2011/06/fxsst.html/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/fxsst.html"
---
examples:
  - description: "Place malicious fxsst.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fxsst.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%WINDIR%\\explorer.exe\""

# fxsst.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %WINDIR%\explorer.exe (Search Order)
