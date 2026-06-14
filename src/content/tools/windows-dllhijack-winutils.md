---
trust_level: community
id: windows-dllhijack-winutils
namespace: windows:dllhijack:winutils
name: winutils.dll
description: "winutils.dll — Sideloading hijacking (Palo Alto)"
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
  template: "winutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2023/rorschach-a-new-sophisticated-and-fast-ransomware/"
  - label: "Reference"
    url: "https://security.paloaltonetworks.com/PAN-SA-2023-0002"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/winutils.html"
---
examples:
  - description: "Place malicious winutils.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Palo Alto Networks\\Traps\\winutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Palo Alto Networks\\Traps\\cydump.exe\""

# winutils.dll

**Vendor:** Palo Alto

**Expected Location:** %PROGRAMFILES%\Palo Alto Networks\Traps

**Vulnerable Executables:**
- %PROGRAMFILES%\Palo Alto Networks\Traps\cydump.exe (Sideloading)
