---
trust_level: community
id: windows-dllhijack-rastls
namespace: windows:dllhijack:rastls
name: rastls.dll
description: "rastls.dll — Sideloading hijacking (Symantec)"
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
  template: "rastls.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://st.drweb.com/static/new-www/news/2020/october/Study_of_the_ShadowPad_APT_backdoor_and_its_relation_to_PlugX_en.pdf"
  - label: "Reference"
    url: "https://vms.drweb.com/virus/?i=21995051"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rastls.html"
---
examples:
  - description: "Place malicious rastls.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Symantec\\Network Connected Devices Auto Setup\\rastls.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Symantec\\Network Connected Devices Auto Setup\\rastlsc.exe\""

# rastls.dll

**Vendor:** Symantec

**Expected Location:** %PROGRAMFILES%\Symantec\Network Connected Devices Auto Setup

**Vulnerable Executables:**
- %PROGRAMFILES%\Symantec\Network Connected Devices Auto Setup\rastlsc.exe (Sideloading)

**Acknowledgement:** Adam
