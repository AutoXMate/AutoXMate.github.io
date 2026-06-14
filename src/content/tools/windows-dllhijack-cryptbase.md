---
trust_level: community
id: windows-dllhijack-cryptbase
namespace: windows:dllhijack:cryptbase
name: cryptbase.dll
description: cryptbase.dll — Sideloading hijacking (Microsoft)
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
  template: cryptbase.dll
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
- label: Reference
  url: https://twitter.com/AndrewOliveau/status/1682185200862625792
- label: Reference
  url: https://twitter.com/BSummerz/status/1860045985919205645
- label: Reference
  url: https://ice-wzl.medium.com/mikrotik-winbox-dll-side-loading-vulnerability-x2-413d371ff5f0
- label: HijackLibs
  url: https://hijacklibs.net/entries/cryptbase.html
features:
- requires-root
---

examples:
  - description: "Place malicious cryptbase.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cryptbase.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\alg.exe\""

# cryptbase.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\alg.exe (Sideloading)
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\disksnapshot.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\filehistory.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\ie4uinit.exe (Sideloading)
- %SYSTEM32%\lpksetup.exe (Sideloading)
- %SYSTEM32%\mfpmp.exe (Sideloading)
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\net1.exe (Sideloading)
- %SYSTEM32%\netplwiz.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\presentationhost.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\resmon.exe (Sideloading)
- %SYSTEM32%\rmactivate.exe (Sideloading)
- %SYSTEM32%\rmactivate_ssp_isv.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\sppextcomobj.exe (Sideloading)
- %SYSTEM32%\stordiag.exe (Sideloading)
- %SYSTEM32%\tzsync.exe (Sideloading)
- %SYSTEM32%\uevappmonitor.exe (Sideloading)
- %SYSTEM32%\useraccountcontrolsettings.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)
- %SYSTEM32%\wscadminui.exe (Sideloading)
- %PROGRAMFILES%\Minecraft Launcher\MinecraftLauncher.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Deployment Toolkit\Bin\Microsoft.BDD.Catalog35.exe (Sideloading)
- winbox64.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Andrew Oliveau

**Acknowledgement:** Will Summerhill

**Acknowledgement:** ice-wzl
