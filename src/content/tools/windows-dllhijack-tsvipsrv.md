---
trust_level: community
id: windows-dllhijack-tsvipsrv
namespace: windows:dllhijack:tsvipsrv
name: tsvipsrv.dll
description: tsvipsrv.dll — Phantom hijacking (Microsoft)
author: Swachchhanda Shrawan Poudel
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: tsvipsrv.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://blog.fox-it.com/2025/09/01/three-lazarus-rats-coming-for-your-cheese/
- label: Reference
  url: https://www.gendigital.com/blog/insights/research/png-steganography-hides-backdoor
- label: HijackLibs
  url: https://hijacklibs.net/entries/tsvipsrv.html
features:
- process-manip
---

examples:
  - description: "Place malicious tsvipsrv.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tsvipsrv.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\svchost.exe\""

# tsvipsrv.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\svchost.exe (Phantom)

**Acknowledgement:** Swachchhanda Shrawan Poudel
