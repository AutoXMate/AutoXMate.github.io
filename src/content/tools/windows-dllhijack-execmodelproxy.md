---
trust_level: community
id: windows-dllhijack-execmodelproxy
namespace: windows:dllhijack:execmodelproxy
name: execmodelproxy.dll
description: execmodelproxy.dll — Environment Variable hijacking (Microsoft)
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
  template: execmodelproxy.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/execmodelproxy.html
features:
- remote
---

examples:
  - description: "Place malicious execmodelproxy.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\execmodelproxy.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\calc.exe\""

# execmodelproxy.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\calc.exe (Environment Variable)

**Acknowledgement:** Wietze
