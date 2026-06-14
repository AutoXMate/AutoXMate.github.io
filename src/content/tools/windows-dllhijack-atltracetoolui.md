---
trust_level: community
id: windows-dllhijack-atltracetoolui
namespace: windows:dllhijack:atltracetoolui
name: atltracetoolui.dll
description: "atltracetoolui.dll — Sideloading hijacking (Microsoft)"
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
  template: "atltracetoolui.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/atltracetoolui.html"
---
examples:
  - description: "Place malicious atltracetoolui.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft Visual Studio 11.0\\Common7\\Tools\\atltracetoolui.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Visual Studio 11.0\\Common7\\Tools\\ATLTraceTool8.exe\""

# atltracetoolui.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft Visual Studio 11.0\Common7\Tools

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Visual Studio 11.0\Common7\Tools\ATLTraceTool8.exe (Sideloading)
