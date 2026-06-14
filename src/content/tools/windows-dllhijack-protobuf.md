---
trust_level: community
id: windows-dllhijack-protobuf
namespace: windows:dllhijack:protobuf
name: protobuf.dll
description: "protobuf.dll — Sideloading hijacking (irzyxa)"
author: "Austin Worline"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "protobuf.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.bluevoyant.com/blog/rift-brigantines-github-lures-deploy-malware"
  - label: "Reference"
    url: "https://github.com/irzyxa/Volume2"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/protobuf.html"
---
examples:
  - description: "Place malicious protobuf.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\protobuf.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Volume2\\Volume2.exe\""

# protobuf.dll

**Vendor:** irzyxa

**Vulnerable Executables:**
- %PROGRAMFILES%\Volume2\Volume2.exe (Sideloading)

**Acknowledgement:** Austin Worline
