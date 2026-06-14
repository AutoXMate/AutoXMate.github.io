---
trust_level: community
id: windows-dllhijack-providers
namespace: windows:dllhijack:providers
name: providers.dll
description: "providers.dll — Phantom hijacking (npm)"
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
  template: "providers.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://blog.aquasec.com/cve-2022-32223-dll-hijacking"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/providers.html"
---
examples:
  - description: "Place malicious providers.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\providers.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\nodejs\\node.exe\""

# providers.dll

**Vendor:** npm

**Vulnerable Executables:**
- %PROGRAMFILES%\nodejs\node.exe (Phantom)
