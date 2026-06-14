---
trust_level: community
id: windows-dllhijack-deviceassociation
namespace: windows:dllhijack:deviceassociation
name: deviceassociation.dll
description: "deviceassociation.dll — Sideloading hijacking (Microsoft)"
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
  template: "deviceassociation.dll"
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
    url: "https://hijacklibs.net/entries/deviceassociation.html"
---
examples:
  - description: "Place malicious deviceassociation.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\deviceassociation.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\eduprintprov.exe\""

# deviceassociation.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\eduprintprov.exe (Sideloading)
- %SYSTEM32%\proximityuxhost.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
