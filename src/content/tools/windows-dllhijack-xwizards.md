---
trust_level: community
id: windows-dllhijack-xwizards
namespace: windows:dllhijack:xwizards
name: xwizards.dll
description: "xwizards.dll — Environment Variable hijacking (Microsoft)"
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
  template: "xwizards.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/xwizards.html"
---
examples:
  - description: "Place malicious xwizards.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\xwizards.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicepairingwizard.exe\""

# xwizards.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicepairingwizard.exe (Environment Variable)
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
