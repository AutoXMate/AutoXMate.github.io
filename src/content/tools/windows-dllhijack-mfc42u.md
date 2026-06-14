---
trust_level: community
id: windows-dllhijack-mfc42u
namespace: windows:dllhijack:mfc42u
name: mfc42u.dll
description: "mfc42u.dll — Sideloading hijacking (Microsoft)"
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
  template: "mfc42u.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mfc42u.html"
---
examples:
  - description: "Place malicious mfc42u.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mfc42u.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicepairingwizard.exe\""

# mfc42u.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicepairingwizard.exe (Sideloading)
- %SYSTEM32%\dirquota.exe (Sideloading)
- %SYSTEM32%\eudcedit.exe (Sideloading)
- %SYSTEM32%\filescrn.exe (Sideloading)
- %SYSTEM32%\ldp.exe (Sideloading)
- %SYSTEM32%\msconfig.exe (Sideloading)
- %SYSTEM32%\msinfo32.exe (Sideloading)
- %SYSTEM32%\mspaint.exe (Sideloading)
- %SYSTEM32%\nlbmgr.exe (Sideloading)
- %SYSTEM32%\shrpubw.exe (Sideloading)
- %SYSTEM32%\storrept.exe (Sideloading)
- %SYSTEM32%\verifiergui.exe (Sideloading)
- %SYSTEM32%\wfs.exe (Sideloading)

**Acknowledgement:** Chris Spehn
