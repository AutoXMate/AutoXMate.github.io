---
trust_level: community
id: windows-dllhijack-desktopshellext
namespace: windows:dllhijack:desktopshellext
name: desktopshellext.dll
description: "desktopshellext.dll — Environment Variable hijacking (Microsoft)"
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
  template: "desktopshellext.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/desktopshellext.html"
---
examples:
  - description: "Place malicious desktopshellext.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\desktopshellext.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\sihost.exe\""

# desktopshellext.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\sihost.exe (Environment Variable)

**Acknowledgement:** Wietze
