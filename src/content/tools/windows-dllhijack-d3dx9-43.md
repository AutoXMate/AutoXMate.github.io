---
trust_level: community
id: windows-dllhijack-d3dx9-43
namespace: windows:dllhijack:d3dx9-43
name: d3dx9_43.dll
description: "d3dx9_43.dll — Sideloading hijacking (Microsoft)"
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
  template: "d3dx9_43.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2023/05/03/doubled-dll-sideloading-dragon-breath/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/d3dx9-43.html"
---
examples:
  - description: "Place malicious d3dx9_43.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\d3dx9_43.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\Temp\\HPDIAGS\\0699814c-9c5f-46ad-8c9d-a1c61a163f2b\\d3dim9.exe\""

# d3dx9_43.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %LOCALAPPDATA%\Temp\HPDIAGS\0699814c-9c5f-46ad-8c9d-a1c61a163f2b\d3dim9.exe (Sideloading)
