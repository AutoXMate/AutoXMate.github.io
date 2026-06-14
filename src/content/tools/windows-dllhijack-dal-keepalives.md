---
trust_level: community
id: windows-dllhijack-dal-keepalives
namespace: windows:dllhijack:dal-keepalives
name: dal_keepalives.dll
description: "dal_keepalives.dll — Sideloading hijacking (Audinate)"
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
  template: "dal_keepalives.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2023/stayin-alive-targeted-attacks-against-telecoms-and-government-ministries-in-asia/"
  - label: "Reference"
    url: "https://www.cisa.gov/news-events/alerts/2025/02/06/cisa-adds-five-known-exploited-vulnerabilities-catalog"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d4bd89ff56b75fc617f83eb858b6dbce7b36376889b07fa0c2417322ca361c30"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dal-keepalives.html"
---
examples:
  - description: "Place malicious dal_keepalives.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\audinate\\shared files\\dal_keepalives.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\audinate\\shared files\\mDnsResponder.exe\""

# dal_keepalives.dll

**Vendor:** Audinate

**Expected Location:** %PROGRAMFILES%\audinate\shared files

**Vulnerable Executables:**
- %PROGRAMFILES%\audinate\shared files\mDnsResponder.exe (Sideloading)
