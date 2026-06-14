---
trust_level: community
id: windows-dllhijack-cabview
namespace: windows:dllhijack:cabview
name: cabview.dll
description: "cabview.dll — Environment Variable hijacking (Microsoft)"
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
  template: "cabview.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cabview.html"
---
examples:
  - description: "Place malicious cabview.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cabview.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\notepad.exe\""

# cabview.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
