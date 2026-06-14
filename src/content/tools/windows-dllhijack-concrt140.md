---
trust_level: community
id: windows-dllhijack-concrt140
namespace: windows:dllhijack:concrt140
name: concrt140.dll
description: "concrt140.dll — Sideloading hijacking (Microsoft)"
author: "Austin Worline"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "concrt140.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.youtube.com/watch?v=uTQIIWsUSHA"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/119910bd40da350fe61397b7eb8b6bc4c1280ff130129b4f5046d7f460c62fac"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/concrt140.html"
---
examples:
  - description: "Place malicious concrt140.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft Visual Studio\\%VERSION%\\Community\\Common7\\IDE\\VC\\vcpackages\\concrt140.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"vcpkgsrv.exe\""

# concrt140.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft Visual Studio\%VERSION%\Community\Common7\IDE\VC\vcpackages

**Vulnerable Executables:**
- vcpkgsrv.exe (Sideloading)

**Acknowledgement:** Austin Worline
