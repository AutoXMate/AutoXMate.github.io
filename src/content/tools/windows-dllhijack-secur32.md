---
trust_level: community
id: windows-dllhijack-secur32
namespace: windows:dllhijack:secur32
name: secur32.dll
description: "secur32.dll — Sideloading, Search Order hijacking (Microsoft)"
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
  template: "secur32.dll"
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
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/"
  - label: "Reference"
    url: "https://twitter.com/hackerfantastic/status/1657549979840307203"
  - label: "Reference"
    url: "https://github.com/hackerhouse-opensource/CompMgmtLauncher_DLL_UACBypass"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/secur32.html"
---
examples:
  - description: "Place malicious secur32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\secur32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appvclient.exe\""

# secur32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appvclient.exe (Sideloading)
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\dsrm.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\gpresult.exe (Sideloading)
- %SYSTEM32%\klist.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading)
- %SYSTEM32%\repadmin.exe (Sideloading)
- %SYSTEM32%\consent.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Search Order)
- %LOCALAPPDATA%\microsoft\onedrive\%VERSION%\microsoft.sharepoint.exe (Search Order)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Matthew Hickey
