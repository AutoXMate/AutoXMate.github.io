---
trust_level: community
id: windows-dllhijack-fvewiz
namespace: windows:dllhijack:fvewiz
name: fvewiz.dll
description: fvewiz.dll — Sideloading hijacking (Microsoft)
author: Chris Spehn
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
- security.privilegeescalation.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
- privilege-escalation
execution:
  template: fvewiz.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/fvewiz.html
features:
- requires-root
---

examples:
  - description: "Place malicious fvewiz.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\fvewiz.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bitlockerwizard.exe\""

# fvewiz.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bitlockerwizard.exe (Sideloading)
- %SYSTEM32%\bitlockerwizardelev.exe (Sideloading) [AutoElevate]

**Acknowledgement:** Chris Spehn
