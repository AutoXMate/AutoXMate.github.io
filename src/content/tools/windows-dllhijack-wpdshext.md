---
trust_level: community
id: windows-dllhijack-wpdshext
namespace: windows:dllhijack:wpdshext
name: wpdshext.dll
description: "wpdshext.dll — Environment Variable hijacking (Microsoft)"
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
  template: "wpdshext.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wpdshext.html"
---
examples:
  - description: "Place malicious wpdshext.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wpdshext.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# wpdshext.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
