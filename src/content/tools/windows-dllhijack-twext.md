---
trust_level: community
id: windows-dllhijack-twext
namespace: windows:dllhijack:twext
name: twext.dll
description: "twext.dll — Environment Variable hijacking (Microsoft)"
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
  template: "twext.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/twext.html"
---
examples:
  - description: "Place malicious twext.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\twext.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# twext.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)

**Acknowledgement:** Wietze
