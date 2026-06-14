---
trust_level: community
id: windows-dllhijack-msvcp140
namespace: windows:dllhijack:msvcp140
name: msvcp140.dll
description: "msvcp140.dll — Sideloading hijacking (Microsoft)"
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
  template: "msvcp140.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/cbaf513e7fd4322b14adcc34b34d793d79076ad310925981548e8d3cff886527"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msvcp140.html"
---
examples:
  - description: "Place malicious msvcp140.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msvcp140.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Java\\%VERSION%\\bin\\jp2launcher.exe\""

# msvcp140.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Java\%VERSION%\bin\jp2launcher.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
