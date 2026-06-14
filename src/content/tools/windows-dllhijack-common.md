---
trust_level: community
id: windows-dllhijack-common
namespace: windows:dllhijack:common
name: common.dll
description: common.dll — Sideloading hijacking (iroot)
author: Jai Minton
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: common.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.herdprotect.com/romasterconnection.exe-61602b5ec9ff4f651e87c9c4a15a7e4cc7c733aa.aspx
- label: Reference
  url: https://www.virustotal.com/gui/file/5aef5d7e917612b6390904f6468c3d0dbcf30345277b3ad0fe79e62fa8003c5b
- label: HijackLibs
  url: https://hijacklibs.net/entries/common.html
features:
- requires-root
---

examples:
  - description: "Place malicious common.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\iroot\\common.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\iroot\\romasterconnection.exe\""

# common.dll

**Vendor:** iroot

**Expected Location:** %PROGRAMFILES%\iroot

**Vulnerable Executables:**
- %PROGRAMFILES%\iroot\romasterconnection.exe (Sideloading)

**Acknowledgement:** Jai Minton
