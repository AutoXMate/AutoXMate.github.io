---
trust_level: community
id: windows-dllhijack-windowscodecs
namespace: windows:dllhijack:windowscodecs
name: windowscodecs.dll
description: "windowscodecs.dll — Sideloading, Environment Variable hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "windowscodecs.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windowscodecs.html"
---
examples:
  - description: "Place malicious windowscodecs.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windowscodecs.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# windowscodecs.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\osk.exe (Sideloading)
- %SYSTEM32%\quickassist.exe (Sideloading)
- %SYSTEM32%\wmpdmc.exe (Sideloading)
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\dfrgui.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\gamepanel.exe (Environment Variable)
- %SYSTEM32%\mstsc.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\presentationsettings.exe (Environment Variable)
- %SYSTEM32%\wfs.exe (Environment Variable)
- %SYSTEM32%\winver.exe (Environment Variable)
- %SYSTEM32%\wordpad.exe (Environment Variable)
- %SYSTEM32%\wscollect.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)

**Acknowledgement:** Wietze
