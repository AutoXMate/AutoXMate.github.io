---
trust_level: community
id: windows-dllhijack-hpcustpartui
namespace: windows:dllhijack:hpcustpartui
name: hpcustpartui.dll
description: "hpcustpartui.dll — Sideloading hijacking (HP)"
author: "Christiaan Beek"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "hpcustpartui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trellix.com/en-us/about/newsroom/stories/research/operation-harvest-a-deep-dive-into-a-long-term-campaign.html"
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/hpcustpartui.html"
---
examples:
  - description: "Place malicious hpcustpartui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\HP\\hpcustpartui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"HPCustParticUI.exe\""

# hpcustpartui.dll

**Vendor:** HP

**Expected Location:** %PROGRAMFILES%\HP

**Vulnerable Executables:**
- HPCustParticUI.exe (Sideloading)

**Acknowledgement:** Christiaan Beek
