---
trust_level: community
id: windows-dllhijack-ntdsapi
namespace: windows:dllhijack:ntdsapi
name: ntdsapi.dll
description: "ntdsapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "ntdsapi.dll"
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
    url: "https://hijacklibs.net/entries/ntdsapi.html"
---
examples:
  - description: "Place malicious ntdsapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ntdsapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certutil.exe\""

# ntdsapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\cipher.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\dnscmd.exe (Sideloading)
- %SYSTEM32%\dsacls.exe (Sideloading)
- %SYSTEM32%\dsadd.exe (Sideloading)
- %SYSTEM32%\dsdbutil.exe (Sideloading)
- %SYSTEM32%\dsget.exe (Sideloading)
- %SYSTEM32%\dsmgmt.exe (Sideloading)
- %SYSTEM32%\dsquery.exe (Sideloading)
- %SYSTEM32%\gpresult.exe (Sideloading)
- %SYSTEM32%\licmgr.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\nltest.exe (Sideloading)
- %SYSTEM32%\ntdsutil.exe (Sideloading)
- %SYSTEM32%\rendom.exe (Sideloading)
- %SYSTEM32%\repadmin.exe (Sideloading)
- %SYSTEM32%\setspn.exe (Sideloading)
- %SYSTEM32%\w32tm.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
