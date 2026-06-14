---
trust_level: community
id: windows-dllhijack-davclnt
namespace: windows:dllhijack:davclnt
name: davclnt.dll
description: "davclnt.dll — Environment Variable hijacking (Microsoft)"
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
  template: "davclnt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/davclnt.html"
---
examples:
  - description: "Place malicious davclnt.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\davclnt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# davclnt.dll

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
