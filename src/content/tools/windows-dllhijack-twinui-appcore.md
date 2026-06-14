---
trust_level: community
id: windows-dllhijack-twinui-appcore
namespace: windows:dllhijack:twinui-appcore
name: twinui.appcore.dll
description: "twinui.appcore.dll — Environment Variable hijacking (Microsoft)"
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
  template: "twinui.appcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/twinui-appcore.html"
---
examples:
  - description: "Place malicious twinui.appcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\twinui.appcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\calc.exe\""

# twinui.appcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\calc.exe (Environment Variable)

**Acknowledgement:** Wietze
