---
trust_level: community
id: windows-dllhijack-qt5network
namespace: windows:dllhijack:qt5network
name: qt5network.dll
description: "qt5network.dll — Sideloading hijacking (Qt)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "qt5network.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://cyble.com/blog/threat-actor-targets-manufacturing-industry-with-malware/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/dc36a3d95d9a476d773b961b15b188aa3aae0e0a875bca8857fca18c691ec250"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/qt5network.html"
---
examples:
  - description: "Place malicious qt5network.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\LSoft Technologies\\Active@ Data Studio\\qt5network.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\LSoft Technologies\\Active@ Password Changer\\PasswordChanger.exe\""

# qt5network.dll

**Vendor:** Qt

**Expected Location:** %PROGRAMFILES%\LSoft Technologies\Active@ Data Studio

**Vulnerable Executables:**
- %PROGRAMFILES%\LSoft Technologies\Active@ Password Changer\PasswordChanger.exe (Sideloading)

**Acknowledgement:** Micah Babinski

**Acknowledgement:** Jai Minton
