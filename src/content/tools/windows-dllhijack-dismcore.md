---
trust_level: community
id: windows-dllhijack-dismcore
namespace: windows:dllhijack:dismcore
name: dismcore.dll
description: "dismcore.dll — Search Order hijacking (Microsoft)"
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
  template: "dismcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://cofense.com/exploiting-unpatched-vulnerability-ave_maria-malware-not-full-grace/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dismcore.html"
---
examples:
  - description: "Place malicious dismcore.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dism\\dismcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\dism.exe\""

# dismcore.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%\dism

**Vulnerable Executables:**
- %SYSTEM32%\dism.exe (Search Order)
