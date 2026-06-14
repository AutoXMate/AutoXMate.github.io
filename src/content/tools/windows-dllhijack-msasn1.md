---
trust_level: community
id: windows-dllhijack-msasn1
namespace: windows:dllhijack:msasn1
name: msasn1.dll
description: "msasn1.dll — Sideloading hijacking (Microsoft)"
author: "ice-wzl"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "msasn1.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://ice-wzl.medium.com/mikrotik-winbox-dll-side-loading-vulnerability-9ed9420bd4d7"
  - label: "Reference"
    url: "https://github.com/pbatard/rufus/issues/1877"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msasn1.html"
---
examples:
  - description: "Place malicious msasn1.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msasn1.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"winbox64.exe\""

# msasn1.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- winbox64.exe (Sideloading)
- winbox.exe (Sideloading)

**Acknowledgement:** ice-wzl
