---
trust_level: community
id: windows-dllhijack-ssp-isv-exe-rsaenh
namespace: windows:dllhijack:ssp-isv-exe-rsaenh
name: ssp_isv.exe_rsaenh.dll
description: "ssp_isv.exe_rsaenh.dll — Environment Variable hijacking (Microsoft)"
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
  template: "ssp_isv.exe_rsaenh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ssp-isv-exe-rsaenh.html"
---
examples:
  - description: "Place malicious ssp_isv.exe_rsaenh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ssp_isv.exe_rsaenh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rmactivate\""

# ssp_isv.exe_rsaenh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rmactivate (Environment Variable)

**Acknowledgement:** Wietze
