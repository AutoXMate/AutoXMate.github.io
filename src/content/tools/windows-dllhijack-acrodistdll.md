---
trust_level: community
id: windows-dllhijack-acrodistdll
namespace: windows:dllhijack:acrodistdll
name: acrodistdll.dll
description: "acrodistdll.dll — Sideloading hijacking (Adobe)"
author: "Pokhlebin Maxim"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "acrodistdll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://go.recordedfuture.com/hubfs/reports/cta-2022-1223.pdf"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/acrodistdll.html"
---
examples:
  - description: "Place malicious acrodistdll.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Adobe\\Acrobat %VERSION%\\Acrobat\\acrodistdll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Adobe\\Acrobat %VERSION%\\Acrobat\\AcroDist.exe\""

# acrodistdll.dll

**Vendor:** Adobe

**Expected Location:** %PROGRAMFILES%\Adobe\Acrobat %VERSION%\Acrobat

**Vulnerable Executables:**
- %PROGRAMFILES%\Adobe\Acrobat %VERSION%\Acrobat\AcroDist.exe (Sideloading)
