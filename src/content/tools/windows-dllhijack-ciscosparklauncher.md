---
trust_level: community
id: windows-dllhijack-ciscosparklauncher
namespace: windows:dllhijack:ciscosparklauncher
name: ciscosparklauncher.dll
description: "ciscosparklauncher.dll — Sideloading hijacking (Cisco)"
author: "Sorina Ionescu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "ciscosparklauncher.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2022/11/03/family-tree-dll-sideloading-cases-may-be-related/"
  - label: "Reference"
    url: "https://www.joesandbox.com/analysis/279535/0/html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ciscosparklauncher.html"
---
examples:
  - description: "Place malicious ciscosparklauncher.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\CiscoSparkLauncher\\ciscosparklauncher.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"CiscoCollabHost.exe\""

# ciscosparklauncher.dll

**Vendor:** Cisco

**Expected Location:** %LOCALAPPDATA%\CiscoSparkLauncher

**Vulnerable Executables:**
- CiscoCollabHost.exe (Sideloading)
