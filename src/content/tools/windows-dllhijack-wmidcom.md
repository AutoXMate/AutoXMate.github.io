---
trust_level: community
id: windows-dllhijack-wmidcom
namespace: windows:dllhijack:wmidcom
name: wmidcom.dll
description: "wmidcom.dll — Environment Variable hijacking (Microsoft)"
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
  template: "wmidcom.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wmidcom.html"
---
examples:
  - description: "Place malicious wmidcom.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wmidcom.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\stordiag.exe\""

# wmidcom.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\stordiag.exe (Environment Variable)

**Acknowledgement:** Wietze
