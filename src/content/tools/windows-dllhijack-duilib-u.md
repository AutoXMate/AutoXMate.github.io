---
trust_level: community
id: windows-dllhijack-duilib-u
namespace: windows:dllhijack:duilib-u
name: duilib_u.dll
description: "duilib_u.dll — Sideloading hijacking (AnyViewer)"
author: "Jose Oregon"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "duilib_u.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e770be8fba337cc01e24c7f059368526a804d2af64136a39bb84adeebcf9cfbc"
  - label: "Reference"
    url: "https://bazaar.abuse.ch/sample/d99d382868e2e1191c2ac403d9985569d18e534883b3c64606d08847d68a96b6/"
  - label: "Reference"
    url: "https://www.anyviewer.com/download.html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/duilib-u.html"
---
examples:
  - description: "Place malicious duilib_u.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\AnyViewer\\duilib_u.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"SplashWin.exe\""

# duilib_u.dll

**Vendor:** AnyViewer

**Expected Location:** %PROGRAMFILES%\AnyViewer

**Vulnerable Executables:**
- SplashWin.exe (Sideloading)

**Acknowledgement:** Jose Oregon

**Acknowledgement:** Austin Worline
