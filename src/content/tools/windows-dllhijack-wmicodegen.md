---
trust_level: community
id: windows-dllhijack-wmicodegen
namespace: windows:dllhijack:wmicodegen
name: wmicodegen.dll
description: "wmicodegen.dll — Sideloading hijacking (Microsoft)"
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
  template: "wmicodegen.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securelist.com/apt41-in-africa/116986/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wmicodegen.html"
---
examples:
  - description: "Place malicious wmicodegen.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows kits\\%VERSION%\\bin\\%VERSION%\\wmicodegen.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\windows kits\\%VERSION%\\bin\\%VERSION%\\convert-moftoprovider.exe\""

# wmicodegen.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows kits\%VERSION%\bin\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\windows kits\%VERSION%\bin\%VERSION%\convert-moftoprovider.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
