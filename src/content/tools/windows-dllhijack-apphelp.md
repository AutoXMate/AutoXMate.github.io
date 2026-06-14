---
trust_level: community
id: windows-dllhijack-apphelp
namespace: windows:dllhijack:apphelp
name: apphelp.dll
description: "apphelp.dll — Sideloading, Search Order hijacking (Microsoft)"
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
  template: "apphelp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/apphelp.html"
---
examples:
  - description: "Place malicious apphelp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\apphelp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# apphelp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\sdbinst.exe (Sideloading)
- %WINDIR%\explorer.exe (Search Order)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
