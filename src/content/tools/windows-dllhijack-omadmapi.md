---
trust_level: community
id: windows-dllhijack-omadmapi
namespace: windows:dllhijack:omadmapi
name: omadmapi.dll
description: "omadmapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "omadmapi.dll"
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
    url: "https://hijacklibs.net/entries/omadmapi.html"
---
examples:
  - description: "Place malicious omadmapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\omadmapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\deviceenroller.exe\""

# omadmapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dmcertinst.exe (Sideloading)
- %SYSTEM32%\dmcfghost.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\hvsievaluator.exe (Sideloading)
- %SYSTEM32%\mdmagent.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\omadmrpc.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
