---
trust_level: community
id: windows-dllhijack-isv-exe-rsaenh
namespace: windows:dllhijack:isv-exe-rsaenh
name: isv.exe_rsaenh.dll
description: "isv.exe_rsaenh.dll — Environment Variable hijacking (Microsoft)"
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
  template: "isv.exe_rsaenh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/isv-exe-rsaenh.html"
---
examples:
  - description: "Place malicious isv.exe_rsaenh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\isv.exe_rsaenh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rmactivate\""

# isv.exe_rsaenh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rmactivate (Environment Variable)

**Acknowledgement:** Wietze
