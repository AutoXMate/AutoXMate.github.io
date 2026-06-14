---
trust_level: community
id: windows-dllhijack-msvcp110-win
namespace: windows:dllhijack:msvcp110-win
name: msvcp110_win.dll
description: "msvcp110_win.dll — Sideloading hijacking (Microsoft)"
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
  template: "msvcp110_win.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msvcp110-win.html"
---
examples:
  - description: "Place malicious msvcp110_win.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msvcp110_win.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\agentactivationruntimestarter.exe\""

# msvcp110_win.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\agentactivationruntimestarter.exe (Sideloading)
- %SYSTEM32%\appidpolicyconverter.exe (Sideloading)
- %SYSTEM32%\dmcertinst.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\locationnotificationwindows.exe (Sideloading)
- %SYSTEM32%\mdmagent.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\provlaunch.exe (Sideloading)
- %SYSTEM32%\provtool.exe (Sideloading)
- %SYSTEM32%\windowsactiondialog.exe (Sideloading)

**Acknowledgement:** Chris Spehn
