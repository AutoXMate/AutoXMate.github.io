---
trust_level: community
id: windows-dllhijack-defragproxy
namespace: windows:dllhijack:defragproxy
name: defragproxy.dll
description: defragproxy.dll — Environment Variable hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: defragproxy.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/defragproxy.html
features:
- remote
---

examples:
  - description: "Place malicious defragproxy.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\defragproxy.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dfrgui.exe\""

# defragproxy.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\dfrgui.exe (Environment Variable)

**Acknowledgement:** Wietze
