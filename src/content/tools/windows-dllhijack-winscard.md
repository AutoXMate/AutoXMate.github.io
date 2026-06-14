---
trust_level: community
id: windows-dllhijack-winscard
namespace: windows:dllhijack:winscard
name: winscard.dll
description: "winscard.dll — Sideloading hijacking (Microsoft)"
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
  template: "winscard.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/winscard.html"
---
examples:
  - description: "Place malicious winscard.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\winscard.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\immersivetpmvscmgrsvr.exe\""

# winscard.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\immersivetpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\rmttpmvscmgrsvr.exe (Sideloading)
- %SYSTEM32%\tpmvscmgrsvr.exe (Sideloading)

**Acknowledgement:** Chris Spehn
