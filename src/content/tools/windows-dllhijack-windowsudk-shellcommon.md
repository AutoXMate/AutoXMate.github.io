---
trust_level: community
id: windows-dllhijack-windowsudk-shellcommon
namespace: windows:dllhijack:windowsudk-shellcommon
name: windowsudk.shellcommon.dll
description: "windowsudk.shellcommon.dll — Environment Variable hijacking (Microsoft)"
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
  template: "windowsudk.shellcommon.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/windowsudk-shellcommon.html"
---
examples:
  - description: "Place malicious windowsudk.shellcommon.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\windowsudk.shellcommon.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\compmgmtlauncher.exe\""

# windowsudk.shellcommon.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\compmgmtlauncher.exe (Environment Variable)
- %SYSTEM32%\explorer.exe (Environment Variable)
- %PROGRAMFILES%\Microsoft\Edge\Application\msedge.exe (Environment Variable)

**Acknowledgement:** Wietze
