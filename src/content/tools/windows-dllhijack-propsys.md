---
trust_level: community
id: windows-dllhijack-propsys
namespace: windows:dllhijack:propsys
name: propsys.dll
description: propsys.dll — Sideloading, Environment Variable hijacking (Microsoft)
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
  template: propsys.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: Reference
  url: https://wietze.github.io/blog/save-the-environment-variables
- label: Reference
  url: https://securityintelligence.com/posts/windows-features-dll-sideloading/
- label: Reference
  url: https://github.com/xforcered/WFH
- label: HijackLibs
  url: https://hijacklibs.net/entries/propsys.html
features:
- process-manip
- requires-root
---

examples:
  - description: "Place malicious propsys.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\propsys.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bootim.exe\""

# propsys.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bootim.exe (Sideloading)
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\colorcpl.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\customshellhost.exe (Sideloading)
- %SYSTEM32%\dpiscaling.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\dxpserver.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\fondue.exe (Sideloading)
- %SYSTEM32%\fxssvc.exe (Sideloading)
- %SYSTEM32%\fxsunatd.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\mobsync.exe (Sideloading)
- %SYSTEM32%\mspaint.exe (Sideloading)
- %SYSTEM32%\netplwiz.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\optionalfeatures.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\pinenrollmentbroker.exe (Sideloading)
- %SYSTEM32%\printbrmui.exe (Sideloading)
- %SYSTEM32%\printui.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\proximityuxhost.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\rdpclip.exe (Sideloading)
- %SYSTEM32%\resmon.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\settingsynchost.exe (Sideloading)
- %SYSTEM32%\slui.exe (Sideloading)
- %SYSTEM32%\synchost.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wfs.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)
- %SYSTEM32%\workfolders.exe (Sideloading)
- %SYSTEM32%\wpnpinst.exe (Sideloading)
- %SYSTEM32%\write.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\cleanmgr.exe (Environment Variable)
- %SYSTEM32%\control.exe (Environment Variable)
- %SYSTEM32%\ddodiag.exe (Environment Variable)
- %SYSTEM32%\dfrgui.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %SYSTEM32%\fxscover.exe (Environment Variable)
- %SYSTEM32%\licensingdiag.exe (Environment Variable)
- %SYSTEM32%\msdt.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\powershell.exe (Environment Variable)
- %SYSTEM32%\presentationsettings.exe (Environment Variable)
- %SYSTEM32%\tabcal.exe (Environment Variable)
- %SYSTEM32%\verifier.exe (Environment Variable)
- %PROGRAMFILES%\Google\Chrome\Application\chrome.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Mozilla Firefox\firefox.exe (Environment Variable)
- %APPDATA%\Zoom\bin\zoom.exe (Environment Variable)
- %PROGRAMFILES%\WindowsApps\MicrosoftTeams%VERSION%\msteams.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\graph.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msoev.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msotd.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
