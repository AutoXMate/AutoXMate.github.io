---
trust_level: community
id: windows-dllhijack-devicepairing
namespace: windows:dllhijack:devicepairing
name: devicepairing.dll
description: "devicepairing.dll — Environment Variable hijacking (Microsoft)"
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
  template: "devicepairing.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/devicepairing.html"
---
examples:
  - description: "Place malicious devicepairing.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\devicepairing.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicepairingwizard.exe\""

# devicepairing.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicepairingwizard.exe (Environment Variable)

**Acknowledgement:** Wietze
