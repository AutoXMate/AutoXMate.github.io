---
trust_level: community
id: windows-dllhijack-offdmpsvc
namespace: windows:dllhijack:offdmpsvc
name: offdmpsvc.dll
description: "offdmpsvc.dll — Phantom hijacking (Microsoft)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "offdmpsvc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/offdmpsvc.html"
---
examples:
  - description: "Place malicious offdmpsvc.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\offdmpsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\wermgr.exe\""

# offdmpsvc.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\wermgr.exe (Phantom)

**Acknowledgement:** Hexacorn
