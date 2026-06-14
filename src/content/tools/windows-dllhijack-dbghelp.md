---
trust_level: community
id: windows-dllhijack-dbghelp
namespace: windows:dllhijack:dbghelp
name: dbghelp.dll
description: "dbghelp.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "dbghelp.dll"
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
    url: "https://hijacklibs.net/entries/dbghelp.html"
---
examples:
  - description: "Place malicious dbghelp.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows kits\\10\\debuggers\\arm\\dbghelp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# dbghelp.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows kits\10\debuggers\arm

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\dxcap.exe (Sideloading)
- %SYSTEM32%\taskkill.exe (Sideloading)
- %SYSTEM32%\tasklist.exe (Sideloading)
- %SYSTEM32%\tracerpt.exe (Sideloading)
- %SYSTEM32%\werfault.exe (Sideloading)
- %SYSTEM32%\bdehdcfg.exe (Environment Variable)
- %SYSTEM32%\deploymentcsphelper.exe (Environment Variable)
- %SYSTEM32%\djoin.exe (Environment Variable)
- %SYSTEM32%\dnscacheugc.exe (Environment Variable)
- %SYSTEM32%\ieunatt.exe (Environment Variable)
- %SYSTEM32%\muiunattend.exe (Environment Variable)
- %SYSTEM32%\netbtugc.exe (Environment Variable)
- %SYSTEM32%\netiougc.exe (Environment Variable)
- %SYSTEM32%\pnpunattend.exe (Environment Variable)
- %SYSTEM32%\reagentc.exe (Environment Variable)
- %SYSTEM32%\setupugc.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
