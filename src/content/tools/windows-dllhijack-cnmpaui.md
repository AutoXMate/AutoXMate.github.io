---
trust_level: community
id: windows-dllhijack-cnmpaui
namespace: windows:dllhijack:cnmpaui
name: cnmpaui.dll
description: "cnmpaui.dll — Sideloading hijacking (Canon)"
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
  template: "cnmpaui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e787f64af048b9cb8a153a0759555785c8fd3ee1e8efbca312a29f2acb1e4011"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cnmpaui.html"
---
examples:
  - description: "Place malicious cnmpaui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Canon\\Canon IJ Printer Assistant Tool\\\\cnmpaui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"cnmpaui.exe\""

# cnmpaui.dll

**Vendor:** Canon

**Expected Location:** %PROGRAMFILES%\Canon\Canon IJ Printer Assistant Tool\

**Vulnerable Executables:**
- cnmpaui.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
