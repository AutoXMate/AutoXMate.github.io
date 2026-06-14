---
trust_level: community
id: windows-dllhijack-rsaenh
namespace: windows:dllhijack:rsaenh
name: rsaenh.dll
description: "rsaenh.dll — Environment Variable hijacking (Microsoft)"
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
  template: "rsaenh.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rsaenh.html"
---
examples:
  - description: "Place malicious rsaenh.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\rsaenh.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# rsaenh.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\disksnapshot.exe (Environment Variable)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\licensingdiag.exe (Environment Variable)
- %SYSTEM32%\lpksetup.exe (Environment Variable)
- %SYSTEM32%\microsoft.uev.synccontroller.exe (Environment Variable)
- %SYSTEM32%\phoneactivate.exe (Environment Variable)
- %SYSTEM32%\powershell.exe (Environment Variable)
- %SYSTEM32%\rmactivate.exe (Environment Variable)
- %SYSTEM32%\scriptrunner.exe (Environment Variable)
- %SYSTEM32%\sppextcomobj.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)
- %SYSTEM32%\tzsync.exe (Environment Variable)
- %SYSTEM32%\uevappmonitor.exe (Environment Variable)
- %SYSTEM32%\useraccountcontrolsettings.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Mozilla Firefox\firefox.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)
- %APPDATA%\Zoom\bin\zoom.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msoadfsb.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\namecontrolserver.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)

**Acknowledgement:** Wietze
