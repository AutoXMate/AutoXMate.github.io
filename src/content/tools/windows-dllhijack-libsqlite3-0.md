---
trust_level: community
id: windows-dllhijack-libsqlite3-0
namespace: windows:dllhijack:libsqlite3-0
name: libsqlite3-0.dll
description: "libsqlite3-0.dll — Sideloading hijacking (SQLite)"
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
  template: "libsqlite3-0.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/506ab08d0a71610793ae2a5c4c26b1eb35fd9e3c8749cd63877b03c205feb48a/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libsqlite3-0.html"
---
examples:
  - description: "Place malicious libsqlite3-0.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\libsqlite3-0.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\FileZilla FTP Client\\filezilla.exe\""

# libsqlite3-0.dll

**Vendor:** SQLite

**Expected Location:** %PROGRAMFILES%

**Vulnerable Executables:**
- %PROGRAMFILES%\FileZilla FTP Client\filezilla.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
