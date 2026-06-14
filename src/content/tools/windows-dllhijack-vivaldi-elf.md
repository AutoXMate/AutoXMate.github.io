---
trust_level: community
id: windows-dllhijack-vivaldi-elf
namespace: windows:dllhijack:vivaldi-elf
name: vivaldi_elf.dll
description: "vivaldi_elf.dll — Sideloading hijacking (Vivaldi)"
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
  template: "vivaldi_elf.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/vizom-malware-targets-brazilian-bank-customers-remote-overlay/"
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vivaldi-elf.html"
---
examples:
  - description: "Place malicious vivaldi_elf.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Vivaldi\\Application\\vivaldi_elf.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\Vivaldi\\Application\\vivaldi.exe\""

# vivaldi_elf.dll

**Vendor:** Vivaldi

**Expected Location:** %LOCALAPPDATA%\Vivaldi\Application

**Vulnerable Executables:**
- %LOCALAPPDATA%\Vivaldi\Application\vivaldi.exe (Sideloading)
