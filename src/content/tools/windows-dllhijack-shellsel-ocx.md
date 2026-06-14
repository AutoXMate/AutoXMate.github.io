---
trust_level: community
id: windows-dllhijack-shellsel-ocx
namespace: windows:dllhijack:shellsel-ocx
name: shellsel.ocx.dll
description: "shellsel.ocx.dll — Sideloading hijacking (Symantec)"
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
  template: "shellsel.ocx.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "Reference"
    url: "https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/shellsel-ocx.html"
---
examples:
  - description: "Place malicious shellsel.ocx.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\shellsel.ocx.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"symantec.exe\""

# shellsel.ocx.dll

**Vendor:** Symantec

**Vulnerable Executables:**
- symantec.exe (Sideloading)
