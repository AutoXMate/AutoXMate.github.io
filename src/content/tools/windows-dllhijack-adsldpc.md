---
trust_level: community
id: windows-dllhijack-adsldpc
namespace: windows:dllhijack:adsldpc
name: adsldpc.dll
description: "adsldpc.dll — Sideloading hijacking (Microsoft)"
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
  template: "adsldpc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/adsldpc.html"
---
examples:
  - description: "Place malicious adsldpc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\adsldpc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\agentservice.exe\""

# adsldpc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\agentservice.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\sppextcomobj.exe (Sideloading)

**Acknowledgement:** Wietze
