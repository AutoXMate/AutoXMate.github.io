---
trust_level: community
id: windows-dllhijack-dsp-bridge-x64
namespace: windows:dllhijack:dsp-bridge-x64
name: dsp_bridge_x64.dll
description: "dsp_bridge_x64.dll — Sideloading hijacking (KuGou)"
author: "Zhangir Ospanov"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "dsp_bridge_x64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://x.com/s0ld133rr/status/2008531599626055984"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dsp-bridge-x64.html"
---
examples:
  - description: "Place malicious dsp_bridge_x64.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dsp_bridge_x64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"bridge_plugin_host_x64.exe\""

# dsp_bridge_x64.dll

**Vendor:** KuGou

**Vulnerable Executables:**
- bridge_plugin_host_x64.exe (Sideloading)
