---
trust_level: community
id: windows-dllhijack-tbb
namespace: windows:dllhijack:tbb
name: tbb.dll
description: "tbb.dll — Sideloading hijacking (Intel)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "tbb.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d6ca9b88d5eb884a761a068700b8bbb509b01bba322ce6086e500e4e6f332adf/detection"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tbb.html"
---
examples:
  - description: "Place malicious tbb.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Adobe\\Adobe Photoshop CC %VERSION%\\tbb.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Adobe\\Adobe Photoshop CC %VERSION%\\AGF3DPrinterDriver.exe\""

# tbb.dll

**Vendor:** Intel

**Expected Location:** %PROGRAMFILES%\Adobe\Adobe Photoshop CC %VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Adobe\Adobe Photoshop CC %VERSION%\AGF3DPrinterDriver.exe (Sideloading)

**Acknowledgement:** Jai Minton
