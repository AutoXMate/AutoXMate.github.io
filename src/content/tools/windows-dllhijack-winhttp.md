---
trust_level: community
id: windows-dllhijack-winhttp
namespace: windows:dllhijack:winhttp
name: winhttp.dll
description: winhttp.dll — Sideloading hijacking (Microsoft)
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
  template: winhttp.dll
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
- label: HijackLibs
  url: https://hijacklibs.net/entries/winhttp.html
features:
- network-intensive
- requires-root
---

examples:
  - description: "Place malicious winhttp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winhttp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cmdl32.exe\""

# winhttp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cmdl32.exe (Sideloading)
- %SYSTEM32%\devicecensus.exe (Sideloading)
- %SYSTEM32%\dmclient.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\mdmdiagnosticstool.exe (Sideloading)
- %SYSTEM32%\msdt.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\mshta.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\musnotification.exe (Sideloading)
- %SYSTEM32%\musnotificationux.exe (Sideloading)
- %SYSTEM32%\musnotifyicon.exe (Sideloading)
- %SYSTEM32%\netsh.exe (Sideloading)
- %SYSTEM32%\pacjsworker.exe (Sideloading)
- %SYSTEM32%\recoverydrive.exe (Sideloading)
- %SYSTEM32%\resetengine.exe (Sideloading)
- %SYSTEM32%\rpcping.exe (Sideloading)
- %SYSTEM32%\sgrmlpac.exe (Sideloading)
- %SYSTEM32%\sihclient.exe (Sideloading)
- %SYSTEM32%\systemreset.exe (Sideloading) [AutoElevate]
- %SYSTEM32%\wkspbroker.exe (Sideloading)
- %PROGRAMFILES%\Minecraft Launcher\MinecraftLauncher.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn

**Acknowledgement:** Andrew Oliveau
