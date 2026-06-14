---
trust_level: community
id: windows-dllhijack-xmllite
namespace: windows:dllhijack:xmllite
name: xmllite.dll
description: "xmllite.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "xmllite.dll"
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
    url: "https://hijacklibs.net/entries/xmllite.html"
---
examples:
  - description: "Place malicious xmllite.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\xmllite.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# xmllite.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\ddodiag.exe (Sideloading)
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dmcfghost.exe (Sideloading)
- %SYSTEM32%\dmclient.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\dxcap.exe (Sideloading)
- %SYSTEM32%\dxpserver.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\mousocoreworker.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\musnotifyicon.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\sppsvc.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tracerpt.exe (Sideloading)
- %SYSTEM32%\upfc.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)
- %SYSTEM32%\vsgraphicsdesktopengine.exe (Sideloading)
- %SYSTEM32%\vsgraphicsremoteengine.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Common Files\Microsoft Shared\ink\InputPersonalization.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Michał Kucharski
