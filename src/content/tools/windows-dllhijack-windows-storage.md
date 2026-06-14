---
trust_level: community
id: windows-dllhijack-windows-storage
namespace: windows:dllhijack:windows-storage
name: windows.storage.dll
description: "windows.storage.dll — Environment Variable hijacking (Microsoft)"
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
  template: "windows.storage.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windows-storage.html"
---
examples:
  - description: "Place malicious windows.storage.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windows.storage.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\calc.exe\""

# windows.storage.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\calc.exe (Environment Variable)
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\control.exe (Environment Variable)
- %SYSTEM32%\dfrgui.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\licensingdiag.exe (Environment Variable)
- %SYSTEM32%\msdt.exe (Environment Variable)
- %SYSTEM32%\mstsc.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\powershell.exe (Environment Variable)
- %SYSTEM32%\presentationsettings.exe (Environment Variable)
- %SYSTEM32%\rdpclip.exe (Environment Variable)
- %SYSTEM32%\tabcal.exe (Environment Variable)
- %SYSTEM32%\verifier.exe (Environment Variable)
- %SYSTEM32%\wfs.exe (Environment Variable)
- %SYSTEM32%\workfolders.exe (Environment Variable)
- %SYSTEM32%\write.exe (Environment Variable)
- %SYSTEM32%\wscollect.exe (Environment Variable)
- %PROGRAMFILES%\Google\Chrome\Application\chrome.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Mozilla Firefox\firefox.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)
- %APPDATA%\Zoom\bin\zoom.exe (Environment Variable)
- %PROGRAMFILES%\WindowsApps\MicrosoftTeams%VERSION%\msteams.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msoev.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msotd.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)

**Acknowledgement:** Wietze
