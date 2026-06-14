---
trust_level: community
id: windows-dllhijack-powrprof
namespace: windows:dllhijack:powrprof
name: powrprof.dll
description: "powrprof.dll — Sideloading hijacking (Microsoft)"
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
  template: "powrprof.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/powrprof.html"
---
examples:
  - description: "Place malicious powrprof.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\powrprof.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fsquirt.exe\""

# powrprof.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fsquirt.exe (Sideloading)
- %SYSTEM32%\msinfo32.exe (Sideloading)
- %SYSTEM32%\printfilterpipelinesvc.exe (Sideloading)
- %SYSTEM32%\sfc.exe (Sideloading)

**Acknowledgement:** Chris Spehn
