---
trust_level: community
id: windows-dllhijack-lmiguardiandll
namespace: windows:dllhijack:lmiguardiandll
name: lmiguardiandll.dll
description: "lmiguardiandll.dll — Sideloading hijacking (LogMeIn)"
author: "Christiaan Beek"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "lmiguardiandll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/StopMalvertisin/status/1610961056163311619"
  - label: "Reference"
    url: "https://blog.osarmor.com/311/lmiguardiansvc-exe-logmein-abused-to-sideload-malicious-dll/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/lmiguardiandll.html"
---
examples:
  - description: "Place malicious lmiguardiandll.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\LogMeIn\\lmiguardiandll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"LMIGuardianSvc.exe\""

# lmiguardiandll.dll

**Vendor:** LogMeIn

**Expected Location:** %PROGRAMFILES%\LogMeIn

**Vulnerable Executables:**
- LMIGuardianSvc.exe (Sideloading)

**Acknowledgement:** Kimberly
