---
trust_level: community
id: windows-dllhijack-p9np
namespace: windows:dllhijack:p9np
name: p9np.dll
description: "p9np.dll — Environment Variable hijacking (Microsoft)"
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
  template: "p9np.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/p9np.html"
---
examples:
  - description: "Place malicious p9np.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\p9np.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# p9np.dll

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
