---
trust_level: community
id: windows-dllhijack-mscoree
namespace: windows:dllhijack:mscoree
name: mscoree.dll
description: "mscoree.dll — Sideloading hijacking (Microsoft)"
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
  template: "mscoree.dll"
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
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mscoree.html"
---
examples:
  - description: "Place malicious mscoree.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mscoree.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\aitstatic.exe\""

# mscoree.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\aitstatic.exe (Sideloading)
- %SYSTEM32%\presentationhost.exe (Sideloading)
- %WINDIR%\Microsoft.NET\Framework\v%VERSION%\applaunch.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
