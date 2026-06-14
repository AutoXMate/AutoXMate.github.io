---
trust_level: community
id: windows-dllhijack-ntlanman
namespace: windows:dllhijack:ntlanman
name: ntlanman.dll
description: "ntlanman.dll — Environment Variable hijacking (Microsoft)"
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
  template: "ntlanman.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ntlanman.html"
---
examples:
  - description: "Place malicious ntlanman.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ntlanman.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# ntlanman.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\msdt.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\powershell.exe (Environment Variable)
- %SYSTEM32%\stordiag.exe (Environment Variable)
- %SYSTEM32%\tabcal.exe (Environment Variable)
- %SYSTEM32%\verifier.exe (Environment Variable)
- %SYSTEM32%\workfolders.exe (Environment Variable)
- %SYSTEM32%\write.exe (Environment Variable)

**Acknowledgement:** Wietze
