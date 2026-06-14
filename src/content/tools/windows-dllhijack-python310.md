---
trust_level: community
id: windows-dllhijack-python310
namespace: windows:dllhijack:python310
name: python310.dll
description: "python310.dll — Sideloading hijacking (Python)"
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
  template: "python310.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/115fba7a9ea7d2e38d042c7fa5f81209e0d712c107ceb2eafe2f27f94c8f6054/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/python310.html"
---
examples:
  - description: "Place malicious python310.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Python310\\python310.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"pythonw.exe\""

# python310.dll

**Vendor:** Python

**Expected Location:** %PROGRAMFILES%\Python310

**Vulnerable Executables:**
- pythonw.exe (Sideloading)
- dwagent.exe (Sideloading)

**Acknowledgement:** Jai Minton
