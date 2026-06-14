---
trust_level: community
id: windows-dllhijack-relay
namespace: windows:dllhijack:relay
name: relay.dll
description: "relay.dll — Sideloading hijacking (Canon)"
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
  template: "relay.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/6122b4ceb394e4a441b4f7ac92745b1aa64b6c83a4101d6d326e130efa5a5d10/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/relay.html"
---
examples:
  - description: "Place malicious relay.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\relay.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"UniversalInstaller.exe\""

# relay.dll

**Vendor:** Canon

**Vulnerable Executables:**
- UniversalInstaller.exe (Sideloading)

**Acknowledgement:** Jai Minton
