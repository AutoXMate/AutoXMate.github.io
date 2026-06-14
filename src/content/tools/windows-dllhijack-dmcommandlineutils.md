---
trust_level: community
id: windows-dllhijack-dmcommandlineutils
namespace: windows:dllhijack:dmcommandlineutils
name: dmcommandlineutils.dll
description: "dmcommandlineutils.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "dmcommandlineutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dmcommandlineutils.html"
---
examples:
  - description: "Place malicious dmcommandlineutils.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dmcommandlineutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\provtool.exe\""

# dmcommandlineutils.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\provtool.exe (Sideloading)

**Acknowledgement:** Chris Spehn
