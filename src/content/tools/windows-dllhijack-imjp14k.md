---
trust_level: community
id: windows-dllhijack-imjp14k
namespace: windows:dllhijack:imjp14k
name: imjp14k.dll
description: "imjp14k.dll — Sideloading hijacking (Microsoft)"
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
  template: "imjp14k.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/"
  - label: "Reference"
    url: "https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/imjp14k.html"
---
examples:
  - description: "Place malicious imjp14k.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\imjp14k.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Common Files\\Microsoft Shared\\IME14\\SHARED\\imecmnt.exe\""

# imjp14k.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Common Files\Microsoft Shared\IME14\SHARED\imecmnt.exe (Sideloading)
