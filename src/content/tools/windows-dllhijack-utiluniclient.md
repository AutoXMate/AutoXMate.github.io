---
trust_level: community
id: windows-dllhijack-utiluniclient
namespace: windows:dllhijack:utiluniclient
name: utiluniclient.dll
description: "utiluniclient.dll — Phantom hijacking (Trend Micro)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "utiluniclient.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://safebreach.com/blog/2019/trend-micro-security-16-dll-search-order-hijacking-and-potential-abuses/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/utiluniclient.html"
---
examples:
  - description: "Place malicious utiluniclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\utiluniclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\trend micro\\amsp\\coreserviceshell.exe\""

# utiluniclient.dll

**Vendor:** Trend Micro

**Vulnerable Executables:**
- %PROGRAMFILES%\trend micro\amsp\coreserviceshell.exe (Phantom) [PrivEsc]
