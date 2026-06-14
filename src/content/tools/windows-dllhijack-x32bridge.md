---
trust_level: community
id: windows-dllhijack-x32bridge
namespace: windows:dllhijack:x32bridge
name: x32bridge.dll
description: "x32bridge.dll — Sideloading hijacking (x64dbg)"
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
  template: "x32bridge.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_th/research/23/b/investigating-the-plugx-trojan-disguised-as-a-legitimate-windows.html"
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2020/11/04/a-new-apt-uses-dll-side-loads-to-killlsomeone/?cmp=30728"
  - label: "Reference"
    url: "https://unit42.paloaltonetworks.com/plugx-variants-in-usbs/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/x32bridge.html"
---
examples:
  - description: "Place malicious x32bridge.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\x32bridge.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"x32dbg.exe\""

# x32bridge.dll

**Vendor:** x64dbg

**Vulnerable Executables:**
- x32dbg.exe (Sideloading)
