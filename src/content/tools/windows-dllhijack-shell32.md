---
trust_level: community
id: windows-dllhijack-shell32
namespace: windows:dllhijack:shell32
name: shell32.dll
description: "shell32.dll — Environment Variable hijacking (Microsoft)"
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
  template: "shell32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/shell32.html"
---
examples:
  - description: "Place malicious shell32.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\shell32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# shell32.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\control.exe (Environment Variable)
- %SYSTEM32%\dpiscaling.exe (Environment Variable)
- %SYSTEM32%\mobsync.exe (Environment Variable)
- %SYSTEM32%\mstsc.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)
- %SYSTEM32%\presentationsettings.exe (Environment Variable)
- %SYSTEM32%\shellappruntime.exe (Environment Variable)
- %SYSTEM32%\wallpaperhost.exe (Environment Variable)

**Acknowledgement:** Wietze
