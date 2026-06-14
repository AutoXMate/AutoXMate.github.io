---
trust_level: community
id: windows-dllhijack-dsreg
namespace: windows:dllhijack:dsreg
name: dsreg.dll
description: "dsreg.dll — Sideloading hijacking (Microsoft)"
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
  template: "dsreg.dll"
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
    url: "https://hijacklibs.net/entries/dsreg.html"
---
examples:
  - description: "Place malicious dsreg.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dsreg.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bitlockerdeviceencryption.exe\""

# dsreg.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bitlockerdeviceencryption.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
