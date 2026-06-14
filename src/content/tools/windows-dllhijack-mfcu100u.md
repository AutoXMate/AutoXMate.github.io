---
trust_level: community
id: windows-dllhijack-mfcu100u
namespace: windows:dllhijack:mfcu100u
name: mfcu100u.dll
description: "mfcu100u.dll — Sideloading hijacking (Tech Smith)"
author: "Josh Allman"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "mfcu100u.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/73670defa750d0a09470356279494a0c947245229d283c42e7ef0f2b8427b847"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mfcu100u.html"
---
examples:
  - description: "Place malicious mfcu100u.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\TechSmith\\Camtasia Studio 8\\mfcu100u.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\TechSmith\\Camtasia Studio 8\\CamMenuMaker.exe\""

# mfcu100u.dll

**Vendor:** Tech Smith

**Expected Location:** %PROGRAMFILES%\TechSmith\Camtasia Studio 8

**Vulnerable Executables:**
- %PROGRAMFILES%\TechSmith\Camtasia Studio 8\CamMenuMaker.exe (Sideloading)

**Acknowledgement:** Josh Allman

**Acknowledgement:** Dipo R
