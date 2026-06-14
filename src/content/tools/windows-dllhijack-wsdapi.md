---
trust_level: community
id: windows-dllhijack-wsdapi
namespace: windows:dllhijack:wsdapi
name: wsdapi.dll
description: "wsdapi.dll — Sideloading hijacking (Microsoft)"
author: "Gary Lobermier"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wsdapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wsdapi.html"
---
examples:
  - description: "Place malicious wsdapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wsdapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Kits\\10\\bin\\%VERSION%\\x64\\wsddebug_host.exe\""

# wsdapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\x64\wsddebug_host.exe (Sideloading)
