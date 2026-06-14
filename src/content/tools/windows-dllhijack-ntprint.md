---
trust_level: community
id: windows-dllhijack-ntprint
namespace: windows:dllhijack:ntprint
name: ntprint.dll
description: ntprint.dll — Search Order hijacking (Microsoft)
author: SanSan
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: ntprint.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.hexacorn.com/blog/2025/10/06/ntprint-exe-lolbin/
- label: HijackLibs
  url: https://hijacklibs.net/entries/ntprint.html
features:
- pipes-stdout
---

examples:
  - description: "Place malicious ntprint.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ntprint.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ntprint.exe\""

# ntprint.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ntprint.exe (Search Order)

**Acknowledgement:** Adam
