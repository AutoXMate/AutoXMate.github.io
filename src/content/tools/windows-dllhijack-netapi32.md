---
trust_level: community
id: windows-dllhijack-netapi32
namespace: windows:dllhijack:netapi32
name: netapi32.dll
description: "netapi32.dll — Sideloading hijacking (Microsoft)"
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
  template: "netapi32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/netapi32.html"
---
examples:
  - description: "Place malicious netapi32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\netapi32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appvclient.exe\""

# netapi32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appvclient.exe (Sideloading)
- %SYSTEM32%\bootcfg.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\dfscmd.exe (Sideloading)
- %SYSTEM32%\dfsdiag.exe (Sideloading)
- %SYSTEM32%\dfsrdiag.exe (Sideloading)
- %SYSTEM32%\dfsutil.exe (Sideloading)
- %SYSTEM32%\dnscmd.exe (Sideloading)
- %SYSTEM32%\dsadd.exe (Sideloading)
- %SYSTEM32%\dsget.exe (Sideloading)
- %SYSTEM32%\dsquery.exe (Sideloading)
- %SYSTEM32%\ie4uinit.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\qappsrv.exe (Sideloading)
- %SYSTEM32%\spaceagent.exe (Sideloading)
- %SYSTEM32%\wbengine.exe (Sideloading)

**Acknowledgement:** Chris Spehn
