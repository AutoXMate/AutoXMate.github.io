---
trust_level: community
id: windows-dllhijack-ktmw32
namespace: windows:dllhijack:ktmw32
name: ktmw32.dll
description: "ktmw32.dll — Sideloading hijacking (Microsoft)"
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
  template: "ktmw32.dll"
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
    url: "https://hijacklibs.net/entries/ktmw32.html"
---
examples:
  - description: "Place malicious ktmw32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ktmw32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ktmutil.exe\""

# ktmw32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ktmutil.exe (Sideloading)
- %SYSTEM32%\msdtc.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\rstrui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\srtasks.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
