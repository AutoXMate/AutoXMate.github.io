---
trust_level: community
id: windows-dllhijack-vcruntime140
namespace: windows:dllhijack:vcruntime140
name: vcruntime140.dll
description: vcruntime140.dll — Sideloading hijacking (Microsoft)
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
  template: vcruntime140.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.zscaler.com/blogs/security-research/european-diplomats-targeted-apt29-cozy-bear-wineloader
- label: Reference
  url: https://cloud.google.com/blog/topics/threat-intelligence/apt29-wineloader-german-political-parties
- label: HijackLibs
  url: https://hijacklibs.net/entries/vcruntime140.html
features:
- process-manip
---

examples:
  - description: "Place malicious vcruntime140.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\vcruntime140.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft SQL Server\\%VERSION%\\Shared\\sqlwriter.exe\""

# vcruntime140.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft SQL Server\%VERSION%\Shared\sqlwriter.exe (Sideloading)
- %PROGRAMFILES%\Microsoft SQL Server\%VERSION%\Shared\SqlDumper.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
