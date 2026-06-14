---
trust_level: community
id: windows-dllhijack-uiautomationcore
namespace: windows:dllhijack:uiautomationcore
name: uiautomationcore.dll
description: "uiautomationcore.dll — Sideloading hijacking (Microsoft)"
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
  template: "uiautomationcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/uiautomationcore.html"
---
examples:
  - description: "Place malicious uiautomationcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\uiautomationcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\gamepanel.exe\""

# uiautomationcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %SYSTEM32%\magnify.exe (Sideloading)

**Acknowledgement:** Wietze
