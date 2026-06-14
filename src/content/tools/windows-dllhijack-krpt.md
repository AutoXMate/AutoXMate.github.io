---
trust_level: community
id: windows-dllhijack-krpt
namespace: windows:dllhijack:krpt
name: krpt.dll
description: "krpt.dll — Sideloading hijacking (Kingsoft)"
author: "Still Hsu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "krpt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/4957a62e019c30c0a79e4d2d4dd854f6e8f6e0aadb606e157525d98ee0ac5096"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/57acd8566e6cc0526e99d0ba450c662b11a5f70b08bcfe0f326654d9f630a1f1"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/krpt.html"
---
examples:
  - description: "Place malicious krpt.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Kingsoft\\WPS Office\\%VERSION%\\office6\\krpt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Kingsoft\\WPS Office\\%VERSION%\\office6\\wpp.exe\""

# krpt.dll

**Vendor:** Kingsoft

**Expected Location:** %PROGRAMFILES%\Kingsoft\WPS Office\%VERSION%\office6

**Vulnerable Executables:**
- %PROGRAMFILES%\Kingsoft\WPS Office\%VERSION%\office6\wpp.exe (Sideloading)

**Acknowledgement:** Still Hsu
