---
trust_level: community
id: windows-dllhijack-dhcpcsvc6
namespace: windows:dllhijack:dhcpcsvc6
name: dhcpcsvc6.dll
description: "dhcpcsvc6.dll — Sideloading hijacking (Microsoft)"
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
  template: "dhcpcsvc6.dll"
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
    url: "https://hijacklibs.net/entries/dhcpcsvc6.html"
---
examples:
  - description: "Place malicious dhcpcsvc6.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dhcpcsvc6.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ipconfig.exe\""

# dhcpcsvc6.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ipconfig.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
