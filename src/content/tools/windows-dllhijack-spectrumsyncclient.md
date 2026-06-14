---
trust_level: community
id: windows-dllhijack-spectrumsyncclient
namespace: windows:dllhijack:spectrumsyncclient
name: spectrumsyncclient.dll
description: spectrumsyncclient.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: spectrumsyncclient.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://wietze.github.io/blog/hijacking-dlls-in-windows
- label: HijackLibs
  url: https://hijacklibs.net/entries/spectrumsyncclient.html
features:
- remote
---

examples:
  - description: "Place malicious spectrumsyncclient.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\spectrumsyncclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\spectrum.exe\""

# spectrumsyncclient.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\spectrum.exe (Sideloading)

**Acknowledgement:** Wietze
