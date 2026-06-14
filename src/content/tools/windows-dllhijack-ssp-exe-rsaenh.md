---
trust_level: community
id: windows-dllhijack-ssp-exe-rsaenh
namespace: windows:dllhijack:ssp-exe-rsaenh
name: ssp.exe_rsaenh.dll
description: "ssp.exe_rsaenh.dll — Environment Variable hijacking (Microsoft)"
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
  template: "ssp.exe_rsaenh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ssp-exe-rsaenh.html"
---
examples:
  - description: "Place malicious ssp.exe_rsaenh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ssp.exe_rsaenh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rmactivate\""

# ssp.exe_rsaenh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rmactivate (Environment Variable)

**Acknowledgement:** Wietze
