---
trust_level: community
id: windows-dllhijack-sapi-onecore
namespace: windows:dllhijack:sapi-onecore
name: sapi_onecore.dll
description: "sapi_onecore.dll — Environment Variable hijacking (Microsoft)"
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
  template: "sapi_onecore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sapi-onecore.html"
---
examples:
  - description: "Place malicious sapi_onecore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sapi_onecore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\devicecensus.exe\""

# sapi_onecore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\devicecensus.exe (Environment Variable)

**Acknowledgement:** Wietze
