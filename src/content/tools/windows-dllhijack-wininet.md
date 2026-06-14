---
trust_level: community
id: windows-dllhijack-wininet
namespace: windows:dllhijack:wininet
name: wininet.dll
description: wininet.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
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
  template: wininet.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/wininet.html
features:
- requires-root
---

examples:
  - description: "Place malicious wininet.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wininet.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appvclient.exe\""

# wininet.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appvclient.exe (Sideloading)
- %SYSTEM32%\browserexport.exe (Sideloading)
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\ie4uinit.exe (Sideloading)
- %SYSTEM32%\logagent.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\presentationhost.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\tokenbrokercookies.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)
- %SYSTEM32%\wksprt.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
