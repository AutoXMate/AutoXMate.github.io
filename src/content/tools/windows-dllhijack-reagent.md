---
trust_level: community
id: windows-dllhijack-reagent
namespace: windows:dllhijack:reagent
name: reagent.dll
description: "reagent.dll — Sideloading hijacking (Microsoft)"
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
  template: "reagent.dll"
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
    url: "https://hijacklibs.net/entries/reagent.html"
---
examples:
  - description: "Place malicious reagent.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\reagent.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# reagent.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\reagentc.exe (Sideloading)
- %SYSTEM32%\recdisc.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\relpost.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
