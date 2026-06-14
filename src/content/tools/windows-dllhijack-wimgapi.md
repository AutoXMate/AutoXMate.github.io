---
trust_level: community
id: windows-dllhijack-wimgapi
namespace: windows:dllhijack:wimgapi
name: wimgapi.dll
description: "wimgapi.dll — Phantom, Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "wimgapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2015/02/23/beyond-good-ol-run-key-part-28/"
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wimgapi.html"
---
examples:
  - description: "Place malicious wimgapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wimgapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\recoverydrive.exe\""

# wimgapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\dism.exe (Phantom)

**Acknowledgement:** Wietze

**Acknowledgement:** Adam

**Acknowledgement:** Chris Spehn
