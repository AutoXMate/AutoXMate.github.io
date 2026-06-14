---
trust_level: community
id: windows-dllhijack-corefoundation
namespace: windows:dllhijack:corefoundation
name: corefoundation.dll
description: "corefoundation.dll — Sideloading hijacking (Apple)"
author: "Matt Anderson - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "corefoundation.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://analyze.intezer.com/analyses/82011cc1-c3df-4c63-9945-8730b0d1cf3e"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/ff5e56c20591a9019eb28b3cab88f5a240657c1c360bf01ad3a6d417fa10b7f5"
  - label: "Reference"
    url: "https://www.joesandbox.com/analysis/1394928/0/html"
  - label: "Reference"
    url: "https://discussions.apple.com/thread/2732037?sortBy=best"
  - label: "Reference"
    url: "https://iosninja.io/dll/download/corefoundation-dll"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/corefoundation.html"
---
examples:
  - description: "Place malicious corefoundation.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Common Files\\Apple\\Apple Application Support\\corefoundation.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\iTunes\\ituneshelper.exe\""

# corefoundation.dll

**Vendor:** Apple

**Expected Location:** %PROGRAMFILES%\Common Files\Apple\Apple Application Support

**Vulnerable Executables:**
- %PROGRAMFILES%\iTunes\ituneshelper.exe (Sideloading)
- %PROGRAMFILES%\QuickTime\QuickTimePlayer.exe (Sideloading)

**Acknowledgement:** Matt Anderson
