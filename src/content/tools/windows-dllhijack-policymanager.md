---
trust_level: community
id: windows-dllhijack-policymanager
namespace: windows:dllhijack:policymanager
name: policymanager.dll
description: policymanager.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
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
  template: policymanager.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/policymanager.html
features:
- requires-root
---

examples:
  - description: "Place malicious policymanager.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\policymanager.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\displayswitch.exe\""

# policymanager.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\displayswitch.exe (Sideloading)
- %SYSTEM32%\easpolicymanagerbrokerhost.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\eduprintprov.exe (Sideloading)
- %SYSTEM32%\hvsievaluator.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\settingsynchost.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)

**Acknowledgement:** Wietze
