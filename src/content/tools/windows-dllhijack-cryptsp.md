---
trust_level: community
id: windows-dllhijack-cryptsp
namespace: windows:dllhijack:cryptsp
name: cryptsp.dll
description: "cryptsp.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "cryptsp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/cryptsp.html"
---
examples:
  - description: "Place malicious cryptsp.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\cryptsp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\bcdedit.exe\""

# cryptsp.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\bcdedit.exe (Sideloading)
- %SYSTEM32%\disksnapshot.exe (Sideloading)
- %SYSTEM32%\genvalobj.exe (Sideloading)
- %SYSTEM32%\omadmclient.exe (Sideloading)
- %SYSTEM32%\rmactivate.exe (Sideloading)
- %SYSTEM32%\rmactivate_isv.exe (Sideloading)
- %SYSTEM32%\rmactivate_ssp.exe (Sideloading)
- %SYSTEM32%\rmactivate_ssp_isv.exe (Sideloading)
- %SYSTEM32%\werfault.exe (Sideloading)

**Acknowledgement:** Chris Spehn
