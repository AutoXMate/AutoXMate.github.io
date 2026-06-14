---
trust_level: community
id: windows-dllhijack-sppc
namespace: windows:dllhijack:sppc
name: sppc.dll
description: "sppc.dll — Sideloading hijacking (Microsoft)"
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
  template: "sppc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sppc.html"
---
examples:
  - description: "Place malicious sppc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sppc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msinfo32.exe\""

# sppc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msinfo32.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\packageinspector.exe (Sideloading)
- %SYSTEM32%\slui.exe (Sideloading)

**Acknowledgement:** Wietze
