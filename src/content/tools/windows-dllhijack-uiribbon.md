---
trust_level: community
id: windows-dllhijack-uiribbon
namespace: windows:dllhijack:uiribbon
name: uiribbon.dll
description: "uiribbon.dll — Environment Variable hijacking (Microsoft)"
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
  template: "uiribbon.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uiribbon.html"
---
examples:
  - description: "Place malicious uiribbon.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\uiribbon.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wordpad.exe\""

# uiribbon.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wordpad.exe (Environment Variable)

**Acknowledgement:** Wietze
