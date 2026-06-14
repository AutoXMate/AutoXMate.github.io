---
trust_level: community
id: windows-dllhijack-wdi
namespace: windows:dllhijack:wdi
name: wdi.dll
description: "wdi.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "wdi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wdi.html"
---
examples:
  - description: "Place malicious wdi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wdi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cofire.exe\""

# wdi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cofire.exe (Sideloading)
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Environment Variable)
- %SYSTEM32%\slui.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
