---
trust_level: community
id: windows-dllhijack-liteskinutils
namespace: windows:dllhijack:liteskinutils
name: liteskinutils.dll
description: "liteskinutils.dll — Sideloading hijacking (ICQ)"
author: "Jai Minton - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "liteskinutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/e5e53392b29b74545e463b65052e0b6b07e8299d709f07501fb0f31b97a679ab/details"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/a278d5604a93e93a5580845da93af6c316a37a4cd35c1fc9348958ae1bebdb90/details"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/104ca4690b0ff17eb55e1330c5baf5580a731b6834f0716c483e646d6030855c/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/010f55aef8ccba2ea1307d934decd577a08fa21547d1db30e01f3ae5ff1cce07/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/liteskinutils.html"
---
examples:
  - description: "Place malicious liteskinutils.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\ICQLite\\liteskinutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\ICQLite\\ICQLite.exe\""

# liteskinutils.dll

**Vendor:** ICQ

**Expected Location:** %PROGRAMFILES%\ICQLite

**Vulnerable Executables:**
- %PROGRAMFILES%\ICQLite\ICQLite.exe (Sideloading)

**Acknowledgement:** Jai Minton
