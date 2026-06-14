---
trust_level: community
id: windows-dllhijack-iviewers
namespace: windows:dllhijack:iviewers
name: iviewers.dll
description: "iviewers.dll — Sideloading hijacking (Microsoft)"
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
  template: "iviewers.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://www.pwc.co.uk/issues/cyber-security-services/research/chasing-shadows.html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iviewers.html"
---
examples:
  - description: "Place malicious iviewers.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\10\\bin\\%VERSION%\\x86\\iviewers.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\bin\\%VERSION%\\x86\\oleview.exe\""

# iviewers.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\x86

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\x86\oleview.exe (Sideloading)
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\x64\oleview.exe (Sideloading)
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\arm64\oleview.exe (Sideloading)
