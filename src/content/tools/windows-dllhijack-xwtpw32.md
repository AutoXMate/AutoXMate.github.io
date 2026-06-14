---
trust_level: community
id: windows-dllhijack-xwtpw32
namespace: windows:dllhijack:xwtpw32
name: xwtpw32.dll
description: "xwtpw32.dll — Environment Variable hijacking (Microsoft)"
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
  template: "xwtpw32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/xwtpw32.html"
---
examples:
  - description: "Place malicious xwtpw32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\xwtpw32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicepairingwizard.exe\""

# xwtpw32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicepairingwizard.exe (Environment Variable)
- %SYSTEM32%\rasphone.exe (Environment Variable)

**Acknowledgement:** Wietze
