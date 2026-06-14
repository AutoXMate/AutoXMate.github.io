---
trust_level: community
id: windows-dllhijack-lpksetupproxyserv
namespace: windows:dllhijack:lpksetupproxyserv
name: lpksetupproxyserv.dll
description: lpksetupproxyserv.dll — Environment Variable hijacking (Microsoft)
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
  template: lpksetupproxyserv.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: HijackLibs
  url: https://hijacklibs.net/entries/lpksetupproxyserv.html
features:
- remote
---

examples:
  - description: "Place malicious lpksetupproxyserv.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\lpksetupproxyserv.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\lpksetup.exe\""

# lpksetupproxyserv.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\lpksetup.exe (Environment Variable)

**Acknowledgement:** Wietze
