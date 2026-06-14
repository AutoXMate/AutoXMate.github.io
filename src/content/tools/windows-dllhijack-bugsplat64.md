---
trust_level: community
id: windows-dllhijack-bugsplat64
namespace: windows:dllhijack:bugsplat64
name: bugsplat64.dll
description: "bugsplat64.dll — Sideloading hijacking (BugSplat)"
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
  template: "bugsplat64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://x.com/ankit_anubhav/status/1895061182689747333"
  - label: "Reference"
    url: "https://bazaar.abuse.ch/sample/97791eba8ac9745155cea4cc1a90e44765a97b840441220ec13c82f719c65f1a/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/bugsplat64.html"
---
examples:
  - description: "Place malicious bugsplat64.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Nitro\\PDF Pro\\\\bugsplat64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"BugSplatHD64.exe\""

# bugsplat64.dll

**Vendor:** BugSplat

**Expected Location:** %PROGRAMFILES%\Nitro\PDF Pro\

**Vulnerable Executables:**
- BugSplatHD64.exe (Sideloading)

**Acknowledgement:** Ankit Anubhav

**Acknowledgement:** Swachchhanda Shrawan Poudel
