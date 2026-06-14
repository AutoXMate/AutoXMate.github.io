---
trust_level: community
id: windows-dllhijack-tmdbg64
namespace: windows:dllhijack:tmdbg64
name: tmdbg64.dll
description: "tmdbg64.dll — Sideloading hijacking (Trend Micro)"
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
  template: "tmdbg64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/5ee36bf41e2604db18a46515139d0c7bee9a6665e968d4b281cac329e26163d0"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tmdbg64.html"
---
examples:
  - description: "Place malicious tmdbg64.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Temp\\ClnExtor\\PCCNT\\tmdbg64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Trend Micro\\Security Agent\\TmPfw.exe\""

# tmdbg64.dll

**Vendor:** Trend Micro

**Expected Location:** %LOCALAPPDATA%\Temp\ClnExtor\PCCNT

**Vulnerable Executables:**
- %PROGRAMFILES%\Trend Micro\Security Agent\TmPfw.exe (Sideloading)

**Acknowledgement:** Still Hsu
