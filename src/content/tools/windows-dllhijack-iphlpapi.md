---
trust_level: community
id: windows-dllhijack-iphlpapi
namespace: windows:dllhijack:iphlpapi
name: iphlpapi.dll
description: iphlpapi.dll — Sideloading, Search Order, Environment Variable hijacking
  (Microsoft)
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
  template: iphlpapi.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: Reference
  url: https://twitter.com/SBousseaden/status/1550903546916311043
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: Reference
  url: https://twitter.com/AndrewOliveau/status/1682185200862625792
- label: Reference
  url: https://x00.zip/playing-with-process-handles/
- label: Reference
  url: https://twitter.com/BSummerz/status/1860045985919205645
- label: Reference
  url: https://ctrlaltintel.com/research/FudCrypt-analysis-1/
- label: Reference
  url: https://learn.microsoft.com/en-us/answers/questions/f46df9f8-a9bb-4d1d-a11c-c0f6d02454b6/onedrivesetupexe-is-a-malware-autoupdate-without
- label: HijackLibs
  url: https://hijacklibs.net/entries/iphlpapi.html
features:
- requires-root
---

examples:
  - description: "Place malicious iphlpapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\iphlpapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\arp.exe\""

# iphlpapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\arp.exe (Sideloading)
- %SYSTEM32%\colorcpl.exe (Sideloading)
- %SYSTEM32%\datausagelivetiletask.exe (Sideloading)
- %SYSTEM32%\dcdiag.exe (Sideloading)
- %SYSTEM32%\devicecensus.exe (Sideloading)
- %SYSTEM32%\dnscacheugc.exe (Sideloading)
- %SYSTEM32%\fxscover.exe (Sideloading)
- %SYSTEM32%\fxssvc.exe (Sideloading)
- %SYSTEM32%\fxsunatd.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\ipconfig.exe (Sideloading)
- %SYSTEM32%\mousocoreworker.exe (Sideloading)
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\nbtstat.exe (Sideloading)
- %SYSTEM32%\net.exe (Sideloading)
- %SYSTEM32%\netbtugc.exe (Sideloading)
- %SYSTEM32%\netiougc.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\netstat.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\pathping.exe (Sideloading)
- %SYSTEM32%\printbrmui.exe (Sideloading)
- %SYSTEM32%\printui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\route.exe (Sideloading)
- %SYSTEM32%\tracert.exe (Sideloading)
- %SYSTEM32%\w32tm.exe (Sideloading)
- %SYSTEM32%\wfs.exe (Sideloading)
- %SYSTEM32%\wifitask.exe (Sideloading)
- %SYSTEM32%\wpnpinst.exe (Sideloading)
- %LOCALAPPDATA%\microsoft\onedrive\onedrive.exe (Search Order)
- %LOCALAPPDATA%\microsoft\onedrive\OneDriveStandaloneUpdater.exe (Search Order)
- %LOCALAPPDATA%\microsoft\teams\current\teams.exe (Search Order)
- %SYSTEM32%\dpiscaling.exe (Environment Variable)
- %SYSTEM32%\rasphone.exe (Environment Variable)
- %SYSTEM32%\slui.exe (Environment Variable)
- %PROGRAMFILES%\Minecraft Launcher\MinecraftLauncher.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Deployment Toolkit\Bin\Microsoft.BDD.Catalog35.exe (Sideloading)
- %LOCALAPPDATA%\Microsoft\OneDrive\Update\OneDriveSetup.exe (Sideloading)
- %PROGRAMFILES%\WindowsApps\Microsoft.MicrosoftOfficeHub_%VERSION%\WebViewHost\WebViewHost.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Samir

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Andrew Oliveau

**Acknowledgement:** Tim Peck

**Acknowledgement:** Will Summerhill

**Acknowledgement:** Josh Allman
