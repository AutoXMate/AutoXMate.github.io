---
trust_level: community
id: windows-dllhijack-ieadvpack
namespace: windows:dllhijack:ieadvpack
name: ieadvpack.dll
description: "ieadvpack.dll — Sideloading hijacking (Microsoft)"
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
  template: "ieadvpack.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ieadvpack.html"
---
examples:
  - description: "Place malicious ieadvpack.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ieadvpack.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\ie4uinit.exe\""

# ieadvpack.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\ie4uinit.exe (Sideloading)

**Acknowledgement:** Wietze
