---
trust_level: community
id: windows-dllhijack-netprofm
namespace: windows:dllhijack:netprofm
name: netprofm.dll
description: "netprofm.dll — Environment Variable hijacking (Microsoft)"
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
  template: "netprofm.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/netprofm.html"
---
examples:
  - description: "Place malicious netprofm.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\netprofm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\fxscover.exe\""

# netprofm.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\fxscover.exe (Environment Variable)
- %SYSTEM32%\rdpclip.exe (Environment Variable)
- %SYSTEM32%\wordpad.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Mozilla Firefox\firefox.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)
- %PROGRAMFILES%\WindowsApps\MicrosoftTeams%VERSION%\msteams.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\clview.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\cnfnot32.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excelcnv.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\graph.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msoia.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msosrec.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msqry32.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\namecontrolserver.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\protocolhandler.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\scanpst.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\sdxhelper.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\setlang.exe (Environment Variable)

**Acknowledgement:** Wietze
