---
trust_level: community
id: windows-dllhijack-sspicli
namespace: windows:dllhijack:sspicli
name: sspicli.dll
description: "sspicli.dll — Sideloading, Environment Variable hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
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
  template: "sspicli.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "Reference"
    url: "https://lab52.io/blog/analyzing-notdoor-inside-apt28s-expanding-arsenal/"
  - label: "Reference"
    url: "https://www.legit4n6.com/OneDrive-SSPICLI-dll-Side-Loading-Proof-of-Concept-264d60e66daf80caa347f437baf5edf3"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sspicli.html"
---
examples:
  - description: "Place malicious sspicli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sspicli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\at.exe\""

# sspicli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\at.exe (Sideloading)
- %SYSTEM32%\bitsadmin.exe (Sideloading)
- %SYSTEM32%\bootcfg.exe (Sideloading)
- %SYSTEM32%\calc.exe (Sideloading)
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\computerdefaults.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\credentialenrollmentmanager.exe (Sideloading)
- %SYSTEM32%\customshellhost.exe (Sideloading)
- %SYSTEM32%\deviceenroller.exe (Sideloading)
- %SYSTEM32%\dialer.exe (Sideloading)
- %SYSTEM32%\driverquery.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\edpcleanup.exe (Sideloading)
- %SYSTEM32%\eduprintprov.exe (Sideloading)
- %SYSTEM32%\eventcreate.exe (Sideloading)
- %SYSTEM32%\fodhelper.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\ftp.exe (Sideloading)
- %SYSTEM32%\getmac.exe (Sideloading)
- %SYSTEM32%\gpresult.exe (Sideloading)
- %SYSTEM32%\iesettingsync.exe (Sideloading)
- %SYSTEM32%\klist.exe (Sideloading)
- %SYSTEM32%\ksetup.exe (Sideloading)
- %SYSTEM32%\ldp.exe (Sideloading)
- %SYSTEM32%\logman.exe (Sideloading)
- %SYSTEM32%\mdeserver.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\msra.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\mtstocom.exe (Sideloading)
- %SYSTEM32%\muiunattend.exe (Sideloading)
- %SYSTEM32%\netdom.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\openfiles.exe (Sideloading)
- %SYSTEM32%\perfmon.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\pinenrollmentbroker.exe (Sideloading)
- %SYSTEM32%\presentationsettings.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\rdpsa.exe (Sideloading)
- %SYSTEM32%\rpcping.exe (Sideloading)
- %SYSTEM32%\runas.exe (Sideloading)
- %SYSTEM32%\sdclt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\setx.exe (Sideloading)
- %SYSTEM32%\shutdown.exe (Sideloading)
- %SYSTEM32%\systeminfo.exe (Sideloading)
- %SYSTEM32%\systemsettingsadminflows.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\takeown.exe (Sideloading)
- %SYSTEM32%\taskkill.exe (Sideloading)
- %SYSTEM32%\tasklist.exe (Sideloading)
- %SYSTEM32%\waitfor.exe (Sideloading)
- %SYSTEM32%\whoami.exe (Sideloading)
- %SYSTEM32%\wkspbroker.exe (Sideloading)
- %SYSTEM32%\wlrmdr.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\rasphone.exe (Environment Variable)
- %LOCALAPPDATA%\Microsoft\OneDrive\OneDrive.exe (Sideloading)
- %PROGRAMFILES%\Microsoft OneDrive\OneDrive.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Terry Liggett
