---
trust_level: community
id: windows-dllhijack-profapi
namespace: windows:dllhijack:profapi
name: profapi.dll
description: "profapi.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "profapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "Reference"
    url: "https://twitter.com/BSummerz/status/1860045985919205645"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/profapi.html"
---
examples:
  - description: "Place malicious profapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\profapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# profapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\immersivetpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\manage-bde.exe (Sideloading)
- %SYSTEM32%\mousocoreworker.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\provtool.exe (Sideloading)
- %SYSTEM32%\rmttpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\tpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)
- %SYSTEM32%\wwahost.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Deployment Toolkit\Bin\Microsoft.BDD.Catalog35.exe (Sideloading)

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Will Summerhill
