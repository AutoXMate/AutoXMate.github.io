---
trust_level: community
id: windows-dllhijack-wptsextensions
namespace: windows:dllhijack:wptsextensions
name: wptsextensions.dll
description: "wptsextensions.dll — Phantom hijacking (Microsoft)"
author: "k4nfr3"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "wptsextensions.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "http://remoteawesomethoughts.blogspot.com/2019/05/windows-10-task-schedulerservice.html"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wptsextensions.html"
---
examples:
  - description: "Place malicious wptsextensions.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\wptsextensions.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\svchost.exe\""

# wptsextensions.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\svchost.exe (Phantom) [PrivEsc]

**Acknowledgement:** itm4n
