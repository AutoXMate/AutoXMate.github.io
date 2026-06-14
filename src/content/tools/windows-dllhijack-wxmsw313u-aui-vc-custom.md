---
trust_level: community
id: windows-dllhijack-wxmsw313u-aui-vc-custom
namespace: windows:dllhijack:wxmsw313u-aui-vc-custom
name: wxmsw313u_aui_vc_custom.dll
description: "wxmsw313u_aui_vc_custom.dll — Sideloading hijacking (wxWidgets)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "wxmsw313u_aui_vc_custom.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://x.com/CyberRaiju/status/1914454438116540702"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/wxmsw313u-aui-vc-custom.html"
---
examples:
  - description: "Place malicious wxmsw313u_aui_vc_custom.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Audacity\\wxmsw313u_aui_vc_custom.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Audacity\\audacity.exe\""

# wxmsw313u_aui_vc_custom.dll

**Vendor:** wxWidgets

**Expected Location:** %PROGRAMFILES%\Audacity

**Vulnerable Executables:**
- %PROGRAMFILES%\Audacity\audacity.exe (Sideloading)

**Acknowledgement:** Jai Minton
