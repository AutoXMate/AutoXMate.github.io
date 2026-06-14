---
trust_level: community
id: windows-dllhijack-dnx-onecore
namespace: windows:dllhijack:dnx-onecore
name: dnx.onecore.dll
description: "dnx.onecore.dll — Sideloading hijacking (Microsoft)"
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
  template: "dnx.onecore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.acronis.com/en/tru/posts/same-packet-different-magic-mustang-panda-hits-indias-banking-sector-and-korea-geopolitics/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dnx-onecore.html"
---
examples:
  - description: "Place malicious dnx.onecore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft Web Tools\\DNX\\\\dnx.onecore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"dnx.exe\""

# dnx.onecore.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft Web Tools\DNX\

**Vulnerable Executables:**
- dnx.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
