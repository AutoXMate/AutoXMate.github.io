---
trust_level: community
id: windows-dllhijack-dnsapi
namespace: windows:dllhijack:dnsapi
name: dnsapi.dll
description: "dnsapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "dnsapi.dll"
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
    url: "https://hijacklibs.net/entries/dnsapi.html"
---
examples:
  - description: "Place malicious dnsapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dnsapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\checknetisolation.exe\""

# dnsapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\checknetisolation.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\dnscmd.exe (Sideloading)
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\ipconfig.exe (Sideloading)
- %SYSTEM32%\lpremove.exe (Sideloading)
- %SYSTEM32%\msdtc.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\nslookup.exe (Sideloading)
- %SYSTEM32%\rendom.exe (Sideloading)
- %SYSTEM32%\repadmin.exe (Sideloading)
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- %SYSTEM32%\setupugc.exe (Sideloading)
- %SYSTEM32%\sihclient.exe (Sideloading)
- %SYSTEM32%\spoolsv.exe (Sideloading)
- %SYSTEM32%\sppextcomobj.exe (Sideloading)
- %SYSTEM32%\systempropertiesadvanced.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tieringengineservice.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
