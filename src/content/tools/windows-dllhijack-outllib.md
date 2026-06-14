---
trust_level: community
id: windows-dllhijack-outllib
namespace: windows:dllhijack:outllib
name: outllib.dll
description: "outllib.dll — Sideloading hijacking (Microsoft)"
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
  template: "outllib.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://medium.com/insomniacs/analysis-walkthrough-fun-clientrun-part-1-b2509344ebe6"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/outllib.html"
---
examples:
  - description: "Place malicious outllib.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft Office\\OFFICE%VERSION%\\outllib.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Office\\OFFICE%VERSION%\\outlook.exe\""

# outllib.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft Office\OFFICE%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Office\OFFICE%VERSION%\outlook.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office\Root\OFFICE%VERSION%\outlook.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office %VERSION%\ClientX86\Root\Office%VERSION%\outlook.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office %VERSION%\ClientX64\Root\Office%VERSION%\outlook.exe (Sideloading)
