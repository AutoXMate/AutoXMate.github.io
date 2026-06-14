---
trust_level: community
id: windows-dllhijack-activeds
namespace: windows:dllhijack:activeds
name: activeds.dll
description: "activeds.dll — Sideloading hijacking (Microsoft)"
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
  template: "activeds.dll"
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
    url: "https://hijacklibs.net/entries/activeds.html"
---
examples:
  - description: "Place malicious activeds.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\activeds.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\applysettingstemplatecatalog.exe\""

# activeds.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\applysettingstemplatecatalog.exe (Sideloading)
- %SYSTEM32%\agentservice.exe (Sideloading)
- %SYSTEM32%\dsadd.exe (Sideloading)
- %SYSTEM32%\dsget.exe (Sideloading)
- %SYSTEM32%\dsmod.exe (Sideloading)
- %SYSTEM32%\dsrm.exe (Sideloading)
- %SYSTEM32%\gpfixup.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
