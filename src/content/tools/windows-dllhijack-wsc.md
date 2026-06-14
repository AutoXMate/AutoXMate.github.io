---
trust_level: community
id: windows-dllhijack-wsc
namespace: windows:dllhijack:wsc
name: wsc.dll
description: "wsc.dll — Search Order hijacking (Avast)"
author: "Matt Green"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wsc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://github.com/netero1010/Vulnerability-Disclosure/tree/main/CVE-2022-AVAST2"
  - label: "Reference"
    url: "https://securelist.com/cycldek-bridging-the-air-gap/97157/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wsc.html"
---
examples:
  - description: "Place malicious wsc.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\AVAST Software\\Avast\\wsc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"wsc_proxy.exe\""

# wsc.dll

**Vendor:** Avast

**Expected Location:** %PROGRAMFILES%\AVAST Software\Avast

**Vulnerable Executables:**
- wsc_proxy.exe (Search Order)
