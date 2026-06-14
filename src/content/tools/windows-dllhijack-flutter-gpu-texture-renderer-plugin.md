---
trust_level: community
id: windows-dllhijack-flutter-gpu-texture-renderer-plugin
namespace: windows:dllhijack:flutter-gpu-texture-renderer-plugin
name: flutter_gpu_texture_renderer_plugin.dll
description: "flutter_gpu_texture_renderer_plugin.dll — Sideloading hijacking (Rustdesk)"
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
  template: "flutter_gpu_texture_renderer_plugin.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/25/a/how-cracks-and-installers-bring-malware-to-your-device.html"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/857e4cb0b41f7aac5494c8554601888c1c82202de3dab7258b2ff322bc94ca43"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/flutter-gpu-texture-renderer-plugin.html"
---
examples:
  - description: "Place malicious flutter_gpu_texture_renderer_plugin.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\rustdesk\\flutter_gpu_texture_renderer_plugin.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\rustdesk\\rustdesk.exe\""

# flutter_gpu_texture_renderer_plugin.dll

**Vendor:** Rustdesk

**Expected Location:** %LOCALAPPDATA%\rustdesk

**Vulnerable Executables:**
- %LOCALAPPDATA%\rustdesk\rustdesk.exe (Sideloading)
