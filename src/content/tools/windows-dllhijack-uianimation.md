---
trust_level: community
id: windows-dllhijack-uianimation
namespace: windows:dllhijack:uianimation
name: uianimation.dll
description: "uianimation.dll — Environment Variable hijacking (Microsoft)"
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
  template: "uianimation.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uianimation.html"
---
examples:
  - description: "Place malicious uianimation.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\uianimation.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cloudnotifications.exe\""

# uianimation.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cloudnotifications.exe (Environment Variable)
- %SYSTEM32%\gamepanel.exe (Environment Variable)

**Acknowledgement:** Wietze
