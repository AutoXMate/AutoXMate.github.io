---
trust_level: community
id: windows-dllhijack-iertutil
namespace: windows:dllhijack:iertutil
name: iertutil.dll
description: "iertutil.dll — Sideloading hijacking (Microsoft)"
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
  template: "iertutil.dll"
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
    url: "https://hijacklibs.net/entries/iertutil.html"
---
examples:
  - description: "Place malicious iertutil.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iertutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\browserexport.exe\""

# iertutil.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\browserexport.exe (Sideloading)
- %SYSTEM32%\cipher.exe (Sideloading)
- %SYSTEM32%\iesettingsync.exe (Sideloading)
- %SYSTEM32%\launchwinapp.exe (Sideloading)
- %SYSTEM32%\microsoftedgebchost.exe (Sideloading)
- %SYSTEM32%\microsoftedgecp.exe (Sideloading)
- %SYSTEM32%\microsoftedgedevtools.exe (Sideloading)
- %SYSTEM32%\microsoftedgesh.exe (Sideloading)
- %SYSTEM32%\wwahost.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
