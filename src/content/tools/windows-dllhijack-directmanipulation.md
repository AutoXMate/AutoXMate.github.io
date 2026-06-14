---
trust_level: community
id: windows-dllhijack-directmanipulation
namespace: windows:dllhijack:directmanipulation
name: directmanipulation.dll
description: "directmanipulation.dll — Environment Variable hijacking (Microsoft)"
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
  template: "directmanipulation.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/directmanipulation.html"
---
examples:
  - description: "Place malicious directmanipulation.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\directmanipulation.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Office\\root\\Office%VERSION%\\excel.exe\""

# directmanipulation.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excelcnv.exe (Environment Variable)

**Acknowledgement:** Wietze
