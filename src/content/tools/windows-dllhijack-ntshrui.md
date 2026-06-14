---
trust_level: community
id: windows-dllhijack-ntshrui
namespace: windows:dllhijack:ntshrui
name: ntshrui.dll
description: "ntshrui.dll — Environment Variable hijacking (Microsoft)"
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
  template: "ntshrui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ntshrui.html"
---
examples:
  - description: "Place malicious ntshrui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ntshrui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# ntshrui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
