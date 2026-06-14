---
trust_level: community
id: windows-dllhijack-webui
namespace: windows:dllhijack:webui
name: webui.dll
description: "webui.dll — Sideloading hijacking (iTop)"
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
  template: "webui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/063d2c12aa8316b242c5beb9dbbf934be7cee9df93b1612de9aa2f1f3084f0da/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/521c0de9a7b2db7d9a65b443dd630a28e2b4e33f8c56336e7630c646aa2cf280/detection"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/webui.html"
---
examples:
  - description: "Place malicious webui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\iTop Screen Recorder\\webui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\iTop Screen Recorder\\iScrPaint.exe\""

# webui.dll

**Vendor:** iTop

**Expected Location:** %PROGRAMFILES%\iTop Screen Recorder

**Vulnerable Executables:**
- %PROGRAMFILES%\iTop Screen Recorder\iScrPaint.exe (Sideloading)

**Acknowledgement:** Jai Minton
