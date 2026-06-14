---
trust_level: community
id: windows-dllhijack-applicationframe
namespace: windows:dllhijack:applicationframe
name: applicationframe.dll
description: applicationframe.dll — Environment Variable hijacking (Microsoft)
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
  template: applicationframe.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/applicationframe.html
features:
- pipes-stdout
---

examples:
  - description: "Place malicious applicationframe.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\applicationframe.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\applicationframehost.exe\""

# applicationframe.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\applicationframehost.exe (Environment Variable)

**Acknowledgement:** Wietze
