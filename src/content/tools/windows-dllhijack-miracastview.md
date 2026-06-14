---
trust_level: community
id: windows-dllhijack-miracastview
namespace: windows:dllhijack:miracastview
name: miracastview.dll
description: "miracastview.dll — Sideloading hijacking (Microsoft)"
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
  template: "miracastview.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2025/04/29/finding-minhook-in-a-sideloading-attack-and-sweden-too/"
  - label: "Reference"
    url: "https://x.com/fromCharCode/status/1030107346230423554"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/miracastview.html"
---
examples:
  - description: "Place malicious miracastview.dll in the search order location"
    command: "copy malicious.dll \"%WINDIR%\\Miracast\\miracastview.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%WINDIR%\\MiraCast\\MiracastView.exe\""

# miracastview.dll

**Vendor:** Microsoft

**Expected Location:** %WINDIR%\Miracast

**Vulnerable Executables:**
- %WINDIR%\MiraCast\MiracastView.exe (Sideloading)
