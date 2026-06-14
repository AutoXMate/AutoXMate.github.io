---
trust_level: community
id: windows-dllhijack-srclient
namespace: windows:dllhijack:srclient
name: srclient.dll
description: "srclient.dll — Sideloading hijacking (Microsoft)"
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
  template: "srclient.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://blog.vonahi.io/srclient-dll-hijacking/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/srclient.html"
---
examples:
  - description: "Place malicious srclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\srclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\srtasks.exe\""

# srclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\srtasks.exe (Sideloading)
- %SYSTEM32%\tiworker.exe (Sideloading)

**Acknowledgement:** Wietze
