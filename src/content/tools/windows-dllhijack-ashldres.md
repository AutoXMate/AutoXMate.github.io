---
trust_level: community
id: windows-dllhijack-ashldres
namespace: windows:dllhijack:ashldres
name: ashldres.dll
description: "ashldres.dll — Sideloading hijacking (McAfee)"
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
  template: "ashldres.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.sophos.com/en-us/medialibrary/PDFs/technical%20papers/sophos-rotten-tomato-campaign.pdf"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ashldres.html"
---
examples:
  - description: "Place malicious ashldres.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\McAfee.com\\VSO\\ashldres.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"mcvsshld.exe\""

# ashldres.dll

**Vendor:** McAfee

**Expected Location:** %PROGRAMFILES%\McAfee.com\VSO

**Vulnerable Executables:**
- mcvsshld.exe (Sideloading)
