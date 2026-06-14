---
trust_level: community
id: windows-dllhijack-siteadv
namespace: windows:dllhijack:siteadv
name: siteadv.dll
description: "siteadv.dll — Sideloading hijacking (McAfee)"
author: "Christiaan Beek"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "siteadv.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.nortonlifelock.com/sites/default/files/2021-10/OPERATION%20EXORCIST%20White%20Paper.pdf"
  - label: "Reference"
    url: "https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/space-pirates-tools-and-connections/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/siteadv.html"
---
examples:
  - description: "Place malicious siteadv.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\SiteAdvisor\\%VERSION%\\siteadv.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"sideadv.exe\""

# siteadv.dll

**Vendor:** McAfee

**Expected Location:** %PROGRAMFILES%\SiteAdvisor\%VERSION%

**Vulnerable Executables:**
- sideadv.exe (Sideloading)

**Acknowledgement:** Christiaan Beek
