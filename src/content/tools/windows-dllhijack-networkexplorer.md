---
trust_level: community
id: windows-dllhijack-networkexplorer
namespace: windows:dllhijack:networkexplorer
name: networkexplorer.dll
description: networkexplorer.dll — Environment Variable hijacking (Microsoft)
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
  template: networkexplorer.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/networkexplorer.html
features:
- network-intensive
---

examples:
  - description: "Place malicious networkexplorer.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\networkexplorer.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# networkexplorer.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
