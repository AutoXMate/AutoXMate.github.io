---
trust_level: community
id: windows-dllhijack-wbemsvc
namespace: windows:dllhijack:wbemsvc
name: wbemsvc.dll
description: "wbemsvc.dll — Environment Variable hijacking (Microsoft)"
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
  template: "wbemsvc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wbemsvc.html"
---
examples:
  - description: "Place malicious wbemsvc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wbem\\wbemsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cttune.exe\""

# wbemsvc.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%\wbem

**Vulnerable Executables:**
- %SYSTEM32%\cttune.exe (Environment Variable)
- %SYSTEM32%\devicecensus.exe (Environment Variable)
- %SYSTEM32%\driverquery.exe (Environment Variable)
- %SYSTEM32%\getmac.exe (Environment Variable)
- %SYSTEM32%\licensingdiag.exe (Environment Variable)
- %SYSTEM32%\msinfo32.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)
- %SYSTEM32%\systeminfo.exe (Environment Variable)
- %SYSTEM32%\tasklist.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excelcnv.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\scanpst.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)

**Acknowledgement:** Wietze
