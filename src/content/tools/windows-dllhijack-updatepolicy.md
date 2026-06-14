---
trust_level: community
id: windows-dllhijack-updatepolicy
namespace: windows:dllhijack:updatepolicy
name: updatepolicy.dll
description: "updatepolicy.dll — Sideloading hijacking (Microsoft)"
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
  template: "updatepolicy.dll"
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
    url: "https://hijacklibs.net/entries/updatepolicy.html"
---
examples:
  - description: "Place malicious updatepolicy.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\updatepolicy.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\mousocoreworker.exe\""

# updatepolicy.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\mousocoreworker.exe (Sideloading)
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\usoclient.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
