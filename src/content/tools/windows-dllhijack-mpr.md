---
trust_level: community
id: windows-dllhijack-mpr
namespace: windows:dllhijack:mpr
name: mpr.dll
description: "mpr.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "mpr.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mpr.html"
---
examples:
  - description: "Place malicious mpr.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mpr.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootcfg.exe\""

# mpr.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootcfg.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\driverquery.exe (Sideloading)
- %SYSTEM32%\dsmgmt.exe (Sideloading)
- %SYSTEM32%\eventcreate.exe (Sideloading)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\getmac.exe (Sideloading)
- %SYSTEM32%\gpresult.exe (Sideloading)
- %SYSTEM32%\iesettingsync.exe (Sideloading)
- %SYSTEM32%\net.exe (Sideloading)
- %SYSTEM32%\ntdsutil.exe (Sideloading)
- %SYSTEM32%\openfiles.exe (Sideloading)
- %SYSTEM32%\pnpunattend.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\repadmin.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading)
- %SYSTEM32%\setupugc.exe (Sideloading)
- %SYSTEM32%\systeminfo.exe (Sideloading)
- %SYSTEM32%\taskkill.exe (Sideloading)
- %SYSTEM32%\waitfor.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
