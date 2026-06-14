---
trust_level: community
id: windows-dllhijack-cabinet
namespace: windows:dllhijack:cabinet
name: cabinet.dll
description: "cabinet.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "cabinet.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cabinet.html"
---
examples:
  - description: "Place malicious cabinet.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cabinet.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# cabinet.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\cmdl32.exe (Sideloading)
- %SYSTEM32%\expand.exe (Sideloading)
- %SYSTEM32%\extrac32.exe (Sideloading)
- %SYSTEM32%\iesettingsync.exe (Sideloading)
- %SYSTEM32%\licensingdiag.exe (Sideloading)
- %SYSTEM32%\makecab.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\plasrv.exe (Sideloading)
- %SYSTEM32%\pnputil.exe (Sideloading)
- %SYSTEM32%\reagentc.exe (Sideloading)
- %SYSTEM32%\recdisc.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\relpost.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\sihclient.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\usocoreworker.exe (Sideloading)
- %SYSTEM32%\wextract.exe (Sideloading)
- %SYSTEM32%\wimserv.exe (Sideloading)
- %SYSTEM32%\wpnpinst.exe (Sideloading)
- %SYSTEM32%\logman.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
