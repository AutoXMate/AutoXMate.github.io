---
trust_level: community
id: windows-dllhijack-avkkid
namespace: windows:dllhijack:avkkid
name: avkkid.dll
description: "avkkid.dll — Sideloading hijacking (G DATA)"
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
  template: "avkkid.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/68eb5590d8ad952215cf54741b0ed6204c19bba4dcb8d704883e007f16de5028"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/avkkid.html"
---
examples:
  - description: "Place malicious avkkid.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\G DATA\\TotalSecurity\\avkkid\\avkkid.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\G DATA\\TotalSecurity\\avkkid\\avkkid.exe\""

# avkkid.dll

**Vendor:** G DATA

**Expected Location:** %PROGRAMFILES%\G DATA\TotalSecurity\avkkid

**Vulnerable Executables:**
- %PROGRAMFILES%\G DATA\TotalSecurity\avkkid\avkkid.exe (Sideloading)
