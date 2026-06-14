---
trust_level: community
id: windows-dllhijack-goopdate
namespace: windows:dllhijack:goopdate
name: goopdate.dll
description: "goopdate.dll — Sideloading hijacking (Dropbox)"
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
  template: "goopdate.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.huntress.com/blog/advanced-persistent-threat-targeting-vietnamese-human-rights-defenders"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/goopdate.html"
---
examples:
  - description: "Place malicious goopdate.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Dropbox\\Update\\goopdate.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"DropboxUpdate.exe\""

# goopdate.dll

**Vendor:** Dropbox

**Expected Location:** %PROGRAMFILES%\Dropbox\Update

**Vulnerable Executables:**
- DropboxUpdate.exe (Sideloading)
- DropboxCrashHandler.exe (Sideloading)

**Acknowledgement:** Jai Minton

**Acknowledgement:** Craig Sweeney
