---
trust_level: community
id: windows-dllhijack-logoncontroller
namespace: windows:dllhijack:logoncontroller
name: logoncontroller.dll
description: "logoncontroller.dll — Environment Variable hijacking (Microsoft)"
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
  template: "logoncontroller.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/logoncontroller.html"
---
examples:
  - description: "Place malicious logoncontroller.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\logoncontroller.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\logonui.exe\""

# logoncontroller.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\logonui.exe (Environment Variable)

**Acknowledgement:** Wietze
