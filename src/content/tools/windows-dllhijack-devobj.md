---
trust_level: community
id: windows-dllhijack-devobj
namespace: windows:dllhijack:devobj
name: devobj.dll
description: devobj.dll — Sideloading hijacking (Microsoft)
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
  template: devobj.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/devobj.html
features:
- requires-root
---

examples:
  - description: "Place malicious devobj.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\devobj.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bthudtask.exe\""

# devobj.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bthudtask.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\chkdsk.exe (Sideloading)
- %SYSTEM32%\chkntfs.exe (Sideloading)
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dispdiag.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\drvinst.exe (Sideloading)
- %SYSTEM32%\fsavailux.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\fsquirt.exe (Sideloading)
- %SYSTEM32%\immersivetpmvscmgrsvr.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\iscsicli.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\label.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\pnputil.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\recover.exe (Sideloading)
- %SYSTEM32%\rmttpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\tabcal.exe (Sideloading)
- %SYSTEM32%\vsgraphicsdesktopengine.exe (Sideloading)
- %SYSTEM32%\vssvc.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
