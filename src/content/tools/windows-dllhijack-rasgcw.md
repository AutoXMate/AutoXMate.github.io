---
trust_level: community
id: windows-dllhijack-rasgcw
namespace: windows:dllhijack:rasgcw
name: rasgcw.dll
description: "rasgcw.dll — Environment Variable hijacking (Microsoft)"
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
  template: "rasgcw.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rasgcw.html"
---
examples:
  - description: "Place malicious rasgcw.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\rasgcw.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\rasphone.exe\""

# rasgcw.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
