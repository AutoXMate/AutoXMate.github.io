---
trust_level: community
id: windows-dllhijack-msvcr100
namespace: windows:dllhijack:msvcr100
name: msvcr100.dll
description: "msvcr100.dll — Sideloading, Search Order hijacking (Microsoft)"
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
  template: "msvcr100.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/SBousseaden/status/1530595156055011330"
  - label: "Reference"
    url: "https://twitter.com/sbousseaden/status/1604934564614381571"
  - label: "Reference"
    url: "https://blog.eclecticiq.com/dark-pink-apt-group-strikes-government-entities-in-south-asian-countries"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msvcr100.html"
---
examples:
  - description: "Place malicious msvcr100.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msvcr100.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Java\\jre%VERSION%\\bin\\javacpl.exe\""

# msvcr100.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Java\jre%VERSION%\bin\javacpl.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Sideloading)
- cleanospp_64.exe (Search Order)

**Acknowledgement:** Samir

**Acknowledgement:** kinako
