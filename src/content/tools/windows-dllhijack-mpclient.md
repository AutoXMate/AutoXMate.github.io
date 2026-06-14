---
trust_level: community
id: windows-dllhijack-mpclient
namespace: windows:dllhijack:mpclient
name: mpclient.dll
description: mpclient.dll — Sideloading hijacking (Microsoft)
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
  template: mpclient.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool/
- label: Reference
  url: https://twitter.com/Sh0ckFR/status/1554021948967079936
- label: HijackLibs
  url: https://hijacklibs.net/entries/mpclient.html
features:
- remote
---

examples:
  - description: "Place malicious mpclient.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Windows Defender\\mpclient.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Windows Defender\\mpcmdrun.exe\""

# mpclient.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Windows Defender

**Vulnerable Executables:**
- %PROGRAMFILES%\Windows Defender\mpcmdrun.exe (Sideloading)
- %PROGRAMFILES%\Windows Defender\nissrv.exe (Sideloading)
- %PROGRAMFILES%\Windows Defender\dlpuseragent.exe (Sideloading)
