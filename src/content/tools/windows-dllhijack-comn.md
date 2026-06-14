---
trust_level: community
id: windows-dllhijack-comn
namespace: windows:dllhijack:comn
name: comn.dll
description: "comn.dll — Sideloading hijacking (AOMEI)"
author: "Still Hsu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "comn.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/2f5e9ef06c1ae2253a50c9556a8a522eaa5dd1e33d2fdc6930ab3c93ae538240"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/comn.html"
---
examples:
  - description: "Place malicious comn.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\AOMEI\\AOMEI Backupper\\%VERSION%\\comn.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\AOMEI\\AOMEI Backupper\\%VERSION%\\Abspawnhlp.exe\""

# comn.dll

**Vendor:** AOMEI

**Expected Location:** %PROGRAMFILES%\AOMEI\AOMEI Backupper\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\AOMEI\AOMEI Backupper\%VERSION%\Abspawnhlp.exe (Sideloading)
- %PROGRAMFILES%\AOMEI\AOMEI Backupper\%VERSION%\ABCorehlp.exe (Sideloading)

**Acknowledgement:** Still Hsu
