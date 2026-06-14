---
trust_level: community
id: windows-dllhijack-msctfmonitor
namespace: windows:dllhijack:msctfmonitor
name: msctfmonitor.dll
description: "msctfmonitor.dll — Sideloading hijacking (Microsoft)"
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
  template: "msctfmonitor.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/msctfmonitor.html"
---
examples:
  - description: "Place malicious msctfmonitor.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\msctfmonitor.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\credwiz.exe\""

# msctfmonitor.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\credwiz.exe (Sideloading)
- %SYSTEM32%\ctfmon.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
