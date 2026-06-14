---
trust_level: community
id: windows-dllhijack-comdlg32
namespace: windows:dllhijack:comdlg32
name: comdlg32.dll
description: "comdlg32.dll — Environment Variable hijacking (Microsoft)"
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
  template: "comdlg32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/comdlg32.html"
---
examples:
  - description: "Place malicious comdlg32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\comdlg32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# comdlg32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
