---
trust_level: community
id: windows-dllhijack-ndfapi
namespace: windows:dllhijack:ndfapi
name: ndfapi.dll
description: "ndfapi.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "ndfapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ndfapi.html"
---
examples:
  - description: "Place malicious ndfapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ndfapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msra.exe\""

# ndfapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Environment Variable)
- %SYSTEM32%\slui.exe (Environment Variable)

**Acknowledgement:** Wietze
