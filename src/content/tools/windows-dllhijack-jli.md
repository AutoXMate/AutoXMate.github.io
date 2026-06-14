---
trust_level: community
id: windows-dllhijack-jli
namespace: windows:dllhijack:jli
name: jli.dll
description: "jli.dll — Sideloading hijacking (Oracle)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "jli.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://lab52.io/blog/snake-keylogger-in-geopolitical-affairs-abuse-of-trusted-java-utilities-in-cybercrime-operations/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/18e3d1542d9d375f2e1d4631e03e9874fca9a1655ee6d01121d0c94e138be174"
  - label: "Reference"
    url: "https://securelist.com/apt41-in-africa/116986/"
  - label: "Reference"
    url: "https://www.proofpoint.com/us/blog/threat-insight/phish-china-aligned-espionage-actors-ramp-up-taiwan-semiconductor-targeting"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/jli.html"
---
examples:
  - description: "Place malicious jli.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Java\\%VERSION%\\bin\\jli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Java\\%VERSION%\\bin\\jsadebugd.exe\""

# jli.dll

**Vendor:** Oracle

**Expected Location:** %PROGRAMFILES%\Java\%VERSION%\bin

**Vulnerable Executables:**
- %PROGRAMFILES%\Java\%VERSION%\bin\jsadebugd.exe (Sideloading)
- %PROGRAMFILES%\Java\%VERSION%\bin\java.exe (Sideloading)
- %PROGRAMFILES%\Java\%VERSION%\bin\javaw.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
