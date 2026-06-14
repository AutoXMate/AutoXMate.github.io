---
trust_level: community
id: windows-dllhijack-utildll
namespace: windows:dllhijack:utildll
name: utildll.dll
description: "utildll.dll — Sideloading hijacking (Microsoft)"
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
  template: "utildll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/utildll.html"
---
examples:
  - description: "Place malicious utildll.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\utildll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\change.exe\""

# utildll.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\change.exe (Sideloading)
- %SYSTEM32%\chglogon.exe (Sideloading)
- %SYSTEM32%\chgport.exe (Sideloading)
- %SYSTEM32%\query.exe (Sideloading)
- %SYSTEM32%\quser.exe (Sideloading)
- %SYSTEM32%\qprocess.exe (Sideloading)
- %SYSTEM32%\qwinsta.exe (Sideloading)
- %SYSTEM32%\reset.exe (Sideloading)
- %SYSTEM32%\rwinsta.exe (Sideloading)
- %SYSTEM32%\tscon.exe (Sideloading)
- %SYSTEM32%\tskill.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
