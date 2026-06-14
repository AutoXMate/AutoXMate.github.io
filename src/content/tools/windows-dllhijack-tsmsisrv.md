---
trust_level: community
id: windows-dllhijack-tsmsisrv
namespace: windows:dllhijack:tsmsisrv
name: tsmsisrv.dll
description: "tsmsisrv.dll — Phantom hijacking (Microsoft)"
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
  template: "tsmsisrv.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.gendigital.com/blog/insights/research/png-steganography-hides-backdoor"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tsmsisrv.html"
---
examples:
  - description: "Place malicious tsmsisrv.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tsmsisrv.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\svchost.exe\""

# tsmsisrv.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\svchost.exe (Phantom)

**Acknowledgement:** Swachchhanda Shrawan Poudel
