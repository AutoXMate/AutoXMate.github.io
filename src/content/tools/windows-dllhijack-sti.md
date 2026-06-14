---
trust_level: community
id: windows-dllhijack-sti
namespace: windows:dllhijack:sti
name: sti.dll
description: "sti.dll — Sideloading hijacking (Microsoft)"
author: "Tim Baker"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "sti.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blog.google/threat-analysis-group/government-backed-actors-exploiting-winrar-vulnerability/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sti.html"
---
examples:
  - description: "Place malicious sti.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sti.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Photo Viewer\\ImagingDevices.exe\""

# sti.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Photo Viewer\ImagingDevices.exe (Sideloading)

**Acknowledgement:** Tim Baker
