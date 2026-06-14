---
trust_level: community
id: windows-dllhijack-appvisvsubsystems64
namespace: windows:dllhijack:appvisvsubsystems64
name: appvisvsubsystems64.dll
description: "appvisvsubsystems64.dll — Sideloading hijacking (Microsoft)"
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
  template: "appvisvsubsystems64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2025/apt29-phishing-campaign/"
  - label: "Reference"
    url: "https://lab52.io/blog/2162-2/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/b0ecfe94a829ef82819a5bec168d313a55e07544c3e20e252239679b2e0f46c9"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/appvisvsubsystems64.html"
---
examples:
  - description: "Place malicious appvisvsubsystems64.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Common Files\\microsoft shared\\ClickToRun\\appvisvsubsystems64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Office\\root\\Office%VERSION%\\winword.exe\""

# appvisvsubsystems64.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Common Files\microsoft shared\ClickToRun

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\winword.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office\root\Office%VERSION%\powerpnt.exe (Sideloading)

**Acknowledgement:** Still Hsu
