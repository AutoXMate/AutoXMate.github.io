---
trust_level: community
id: windows-dllhijack-atl71
namespace: windows:dllhijack:atl71
name: atl71.dll
description: "atl71.dll — Sideloading hijacking (Xunlei)"
author: "Jai Minton - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "atl71.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/07ff27bfc879ad9f4d90f17c755c89d2fc3a84994c2304ee3cd79eb84674b9c0/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d42dc50226c59ab41afb691a0d94fa4e141702b678d8bd2fdaaaecb43a8e5b4b/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/atl71.html"
---
examples:
  - description: "Place malicious atl71.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Common Files\\Thunder Network\\TP\\%VERSION%\\atl71.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Common Files\\Thunder Network\\TP\\%VERSION%\\XLBugReport.exe\""

# atl71.dll

**Vendor:** Xunlei

**Expected Location:** %PROGRAMFILES%\Common Files\Thunder Network\TP\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Common Files\Thunder Network\TP\%VERSION%\XLBugReport.exe (Sideloading)

**Acknowledgement:** Jai Minton
