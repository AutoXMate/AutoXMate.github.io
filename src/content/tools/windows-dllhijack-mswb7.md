---
trust_level: community
id: windows-dllhijack-mswb7
namespace: windows:dllhijack:mswb7
name: mswb7.dll
description: "mswb7.dll — Environment Variable hijacking (Microsoft)"
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
  template: "mswb7.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mswb7.html"
---
examples:
  - description: "Place malicious mswb7.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\mswb7.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\control.exe\""

# mswb7.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\control.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)

**Acknowledgement:** Wietze
