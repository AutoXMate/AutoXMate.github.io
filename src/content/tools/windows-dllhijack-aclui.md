---
trust_level: community
id: windows-dllhijack-aclui
namespace: windows:dllhijack:aclui
name: aclui.dll
description: "aclui.dll — Sideloading hijacking (Microsoft)"
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
  template: "aclui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2016/03/10/beyond-good-ol-run-key-part-36/"
  - label: "Reference"
    url: "https://www.contextis.com/en/blog/dll-search-order-hijacking"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/aclui.html"
---
examples:
  - description: "Place malicious aclui.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\aclui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\shrpubw.exe\""

# aclui.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\shrpubw.exe (Sideloading)
- %PROGRAMFILES%\Windows Kits\10\bin\%VERSION%\x86\oleview.exe (Sideloading)

**Acknowledgement:** Adam

**Acknowledgement:** Lampros Noutsos

**Acknowledgement:** Chris Spehn
