---
trust_level: community
id: windows-dllhijack-windowscodecsext
namespace: windows:dllhijack:windowscodecsext
name: windowscodecsext.dll
description: "windowscodecsext.dll — Environment Variable hijacking (Microsoft)"
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
  template: "windowscodecsext.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windowscodecsext.html"
---
examples:
  - description: "Place malicious windowscodecsext.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windowscodecsext.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wfs.exe\""

# windowscodecsext.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\wfs.exe (Environment Variable)

**Acknowledgement:** Wietze
