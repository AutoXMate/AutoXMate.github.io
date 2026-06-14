---
trust_level: community
id: windows-dllhijack-vftrace
namespace: windows:dllhijack:vftrace
name: vftrace.dll
description: "vftrace.dll — Sideloading hijacking (CyberArk)"
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
  template: "vftrace.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/budworm-espionage-us-state?web_view=true"
  - label: "Reference"
    url: "https://www.cisa.gov/uscert/ncas/analysis-reports/ar22-277b"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vftrace.html"
---
examples:
  - description: "Place malicious vftrace.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\CyberArk\\Endpoint Privilege Manager\\Agent\\x32\\vftrace.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"vf_host.exe\""

# vftrace.dll

**Vendor:** CyberArk

**Expected Location:** %PROGRAMFILES%\CyberArk\Endpoint Privilege Manager\Agent\x32

**Vulnerable Executables:**
- vf_host.exe (Sideloading)

**Acknowledgement:** Threat Hunting Team Symantec

**Acknowledgement:** CISA
