---
trust_level: community
id: windows-dllhijack-ncrypt
namespace: windows:dllhijack:ncrypt
name: ncrypt.dll
description: "ncrypt.dll — Sideloading, Environment Variable hijacking (Microsoft)"
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
  template: "ncrypt.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/save-the-environment-variables"
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ncrypt.html"
---
examples:
  - description: "Place malicious ncrypt.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\ncrypt.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\certreq.exe\""

# ncrypt.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\certreq.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\clipup.exe (Sideloading)
- %SYSTEM32%\dmcertinst.exe (Sideloading)
- %SYSTEM32%\dnscmd.exe (Sideloading)
- %SYSTEM32%\dsregcmd.exe (Sideloading)
- %SYSTEM32%\filehistory.exe (Environment Variable)
- %SYSTEM32%\sgrmbroker.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Chris Spehn
