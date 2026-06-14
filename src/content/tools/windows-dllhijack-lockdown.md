---
trust_level: community
id: windows-dllhijack-lockdown
namespace: windows:dllhijack:lockdown
name: lockdown.dll
description: "lockdown.dll — Sideloading hijacking (McAfee)"
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
  template: "lockdown.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/thepacketrat/status/1520878930449817600"
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2021/10/04/atom-silo-ransomware-actors-use-confluence-exploit-dll-side-load-for-stealthy-attack/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/lockdown.html"
---
examples:
  - description: "Place malicious lockdown.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\McAfee\\VirusScan Enterprise\\lockdown.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"mfeann.exe\""

# lockdown.dll

**Vendor:** McAfee

**Expected Location:** %PROGRAMFILES%\McAfee\VirusScan Enterprise

**Vulnerable Executables:**
- mfeann.exe (Sideloading)

**Acknowledgement:** Sean Gallagher
