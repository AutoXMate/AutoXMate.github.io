---
trust_level: community
id: windows-dllhijack-mpsvc
namespace: windows:dllhijack:mpsvc
name: mpsvc.dll
description: mpsvc.dll — Sideloading hijacking (Microsoft)
author: Wietze Beukema
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: mpsvc.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.mcafee.com/blogs/other-blogs/mcafee-labs/revil-ransomware-uses-dll-sideloading/
- label: Reference
  url: https://news.sophos.com/en-us/2020/11/04/a-new-apt-uses-dll-side-loads-to-killlsomeone/
- label: Reference
  url: https://www.fortinet.com/blog/threat-research/dll-side-loading-technique-used-in-recent-kaseya-ransomware-attack
- label: HijackLibs
  url: https://hijacklibs.net/entries/mpsvc.html
features:
- process-manip
---

examples:
  - description: "Place malicious mpsvc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMDATA%\\Microsoft\\Windows Defender\\Platform\\%VERSION%\\mpsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMDATA%\\Microsoft\\Windows Defender\\Platform\\%VERSION%\\MsMpEng.exe\""

# mpsvc.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMDATA%\Microsoft\Windows Defender\Platform\%VERSION%

**Vulnerable Executables:**
- %PROGRAMDATA%\Microsoft\Windows Defender\Platform\%VERSION%\MsMpEng.exe (Sideloading)
