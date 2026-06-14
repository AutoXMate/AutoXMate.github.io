---
trust_level: community
id: windows-dllhijack-quickdeskband
namespace: windows:dllhijack:quickdeskband
name: quickdeskband.dll
description: "quickdeskband.dll — Sideloading hijacking (Lenovo)"
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
  template: "quickdeskband.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/StopMalvertisin/status/1722939123470848279"
  - label: "Reference"
    url: "https://twitter.com/RexorVc0/status/1811280904662257907"
  - label: "Reference"
    url: "https://mp.weixin.qq.com/s/IB2w86cXcpmGS8qrOnprKw"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/quickdeskband.html"
---
examples:
  - description: "Place malicious quickdeskband.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\quickdeskband.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"lenovodesk.exe\""

# quickdeskband.dll

**Vendor:** Lenovo

**Vulnerable Executables:**
- lenovodesk.exe (Sideloading)
