---
trust_level: community
id: windows-dllhijack-eappcfg
namespace: windows:dllhijack:eappcfg
name: eappcfg.dll
description: "eappcfg.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "eappcfg.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/eappcfg.html"
---
examples:
  - description: "Place malicious eappcfg.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\eappcfg.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\netsh.exe\""

# eappcfg.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
