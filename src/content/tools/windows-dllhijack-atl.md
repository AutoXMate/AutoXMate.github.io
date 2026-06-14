---
trust_level: community
id: windows-dllhijack-atl
namespace: windows:dllhijack:atl
name: atl.dll
description: "atl.dll — Sideloading hijacking (Microsoft)"
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
  template: "atl.dll"
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
    url: "https://hijacklibs.net/entries/atl.html"
---
examples:
  - description: "Place malicious atl.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\atl.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dsquery.exe\""

# atl.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dsquery.exe (Sideloading)
- %SYSTEM32%\filescrn.exe (Sideloading)
- %SYSTEM32%\msconfig.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\msinfo32.exe (Sideloading)
- %SYSTEM32%\perfmon.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\storrept.exe (Sideloading)
- %SYSTEM32%\vds.exe (Sideloading)
- %SYSTEM32%\vdsldr.exe (Sideloading)
- %SYSTEM32%\vssadmin.exe (Sideloading)
- %SYSTEM32%\wfs.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
