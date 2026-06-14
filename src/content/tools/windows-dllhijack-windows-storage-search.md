---
trust_level: community
id: windows-dllhijack-windows-storage-search
namespace: windows:dllhijack:windows-storage-search
name: windows.storage.search.dll
description: "windows.storage.search.dll — Environment Variable hijacking (Microsoft)"
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
  template: "windows.storage.search.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windows-storage-search.html"
---
examples:
  - description: "Place malicious windows.storage.search.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windows.storage.search.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# windows.storage.search.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Environment Variable)
- %SYSTEM32%\control.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %SYSTEM32%\notepad.exe (Environment Variable)

**Acknowledgement:** Wietze
