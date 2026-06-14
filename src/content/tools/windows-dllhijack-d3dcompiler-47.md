---
trust_level: community
id: windows-dllhijack-d3dcompiler-47
namespace: windows:dllhijack:d3dcompiler-47
name: d3dcompiler_47.dll
description: "d3dcompiler_47.dll — Sideloading hijacking (Microsoft)"
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
  template: "d3dcompiler_47.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/d3dcompiler-47.html"
---
examples:
  - description: "Place malicious d3dcompiler_47.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\windows kits\\10\\bin\\%VERSION%\\x64\\d3dcompiler_47.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dwm.exe\""

# d3dcompiler_47.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\windows kits\10\bin\%VERSION%\x64

**Vulnerable Executables:**
- %SYSTEM32%\dwm.exe (Sideloading)

**Acknowledgement:** Wietze
