---
trust_level: community
id: windows-dllhijack-cryptnet
namespace: windows:dllhijack:cryptnet
name: cryptnet.dll
description: "cryptnet.dll — Sideloading hijacking (Microsoft)"
author: "Will Summerhill"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "cryptnet.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/BSummerz/status/1860045985919205645"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cryptnet.html"
---
examples:
  - description: "Place malicious cryptnet.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cryptnet.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Deployment Toolkit\\Bin\\Microsoft.BDD.Catalog35.exe\""

# cryptnet.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Deployment Toolkit\Bin\Microsoft.BDD.Catalog35.exe (Sideloading)

**Acknowledgement:** Will Summerhill
