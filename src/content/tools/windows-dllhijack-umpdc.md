---
trust_level: community
id: windows-dllhijack-umpdc
namespace: windows:dllhijack:umpdc
name: umpdc.dll
description: "umpdc.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "umpdc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/umpdc.html"
---
examples:
  - description: "Place malicious umpdc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\umpdc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\deviceenroller.exe\""

# umpdc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dmcertinst.exe (Sideloading)
- %SYSTEM32%\iesettingsync.exe (Sideloading)
- %SYSTEM32%\mousocoreworker.exe (Sideloading)
- %SYSTEM32%\netevtfwdr.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\settingsynchost.exe (Sideloading)
- %SYSTEM32%\usocoreworker.exe (Sideloading)
- %SYSTEM32%\wifitask.exe (Sideloading)
- %SYSTEM32%\runtimebroker.exe (Sideloading)

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Michał Kucharski
