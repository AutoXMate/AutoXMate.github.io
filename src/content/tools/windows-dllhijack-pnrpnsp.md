---
trust_level: community
id: windows-dllhijack-pnrpnsp
namespace: windows:dllhijack:pnrpnsp
name: pnrpnsp.dll
description: "pnrpnsp.dll — Environment Variable hijacking (Microsoft)"
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
  template: "pnrpnsp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/pnrpnsp.html"
---
examples:
  - description: "Place malicious pnrpnsp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\pnrpnsp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ftp.exe\""

# pnrpnsp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ftp.exe (Environment Variable)
- %SYSTEM32%\hostname.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)

**Acknowledgement:** Wietze
