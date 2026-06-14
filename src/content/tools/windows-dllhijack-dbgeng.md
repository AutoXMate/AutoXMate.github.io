---
trust_level: community
id: windows-dllhijack-dbgeng
namespace: windows:dllhijack:dbgeng
name: dbgeng.dll
description: "dbgeng.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "dbgeng.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/mrexodia/status/1630320327967252483"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dbgeng.html"
---
examples:
  - description: "Place malicious dbgeng.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Kits\\%VERSION%\\Debuggers\\x86\\dbgeng.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"windbg.exe\""

# dbgeng.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Kits\%VERSION%\Debuggers\x86

**Vulnerable Executables:**
- windbg.exe (Sideloading)

**Acknowledgement:** Duncan Ogilvie
