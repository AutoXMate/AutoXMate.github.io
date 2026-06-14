---
trust_level: community
id: windows-dllhijack-userenv
namespace: windows:dllhijack:userenv
name: userenv.dll
description: userenv.dll — Sideloading hijacking (Microsoft)
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
  template: userenv.dll
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
  url: https://hijacklibs.net/entries/userenv.html
features:
- requires-root
---

examples:
  - description: "Place malicious userenv.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\userenv.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\appidpolicyconverter.exe\""

# userenv.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\appidpolicyconverter.exe (Sideloading)
- %SYSTEM32%\appvclient.exe (Sideloading)
- %SYSTEM32%\appvshnotify.exe (Sideloading)
- %SYSTEM32%\bdeuisrv.exe (Sideloading)
- %SYSTEM32%\colorcpl.exe (Sideloading)
- %SYSTEM32%\customshellhost.exe (Sideloading)
- %SYSTEM32%\dccw.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dmomacpmo.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\gpupdate.exe (Sideloading)
- %SYSTEM32%\mdmappinstaller.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\microsoftedgebchost.exe (Sideloading)
- %SYSTEM32%\microsoftedgecp.exe (Sideloading)
- %SYSTEM32%\microsoftedgesh.exe (Sideloading)
- %SYSTEM32%\mrt.exe (Sideloading)
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\proquota.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\runexehelper.exe (Sideloading)
- %SYSTEM32%\securityhealthservice.exe (Sideloading)
- %SYSTEM32%\settingsynchost.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\tttracer.exe (Sideloading)
- %SYSTEM32%\utcdecoderhost.exe (Sideloading)
- %SYSTEM32%\vaultcmd.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\wpcmon.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
