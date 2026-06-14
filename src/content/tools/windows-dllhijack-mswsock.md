---
trust_level: community
id: windows-dllhijack-mswsock
namespace: windows:dllhijack:mswsock
name: mswsock.dll
description: "mswsock.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "mswsock.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mswsock.html"
---
examples:
  - description: "Place malicious mswsock.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mswsock.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\alg.exe\""

# mswsock.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\alg.exe (Sideloading)
- %SYSTEM32%\curl.exe (Environment Variable)
- %SYSTEM32%\devicecensus.exe (Environment Variable)
- %SYSTEM32%\finger.exe (Sideloading)
- %SYSTEM32%\fsquirt.exe (Sideloading)
- %SYSTEM32%\ftp.exe (Environment Variable)
- %SYSTEM32%\hostname.exe (Environment Variable)
- %SYSTEM32%\nbtstat.exe (Sideloading)
- %SYSTEM32%\nslookup.exe (Environment Variable)
- %SYSTEM32%\rpcping.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)
- %PROGRAMFILES%\Google\Chrome\Application\chrome.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)
- %PROGRAMFILES%\Mozilla Firefox\firefox.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\excel.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\outlook.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Environment Variable)
- %APPDATA%\Zoom\bin\zoom.exe (Environment Variable)
- %PROGRAMFILES%\WindowsApps\MicrosoftTeams%VERSION%\msteams.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\EdgeWebView\Application\%VERSION%\msedgewebview2.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\msaccess.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\mspub.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\onenote.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\scanpst.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\sdxhelper.exe (Environment Variable)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
