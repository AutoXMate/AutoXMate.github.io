---
trust_level: community
id: windows-dllhijack-sensapi
namespace: windows:dllhijack:sensapi
name: sensapi.dll
description: "sensapi.dll — Sideloading hijacking (Microsoft)"
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
  template: "sensapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/AndrewOliveau/status/1682185200862625792"
  - label: "Reference"
    url: "https://www.fortinet.com/blog/threat-research/nailaolocker-ransomware-cheese"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sensapi.html"
---
examples:
  - description: "Place malicious sensapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\sensapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Minecraft Launcher\\MinecraftLauncher.exe\""

# sensapi.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %PROGRAMFILES%\Minecraft Launcher\MinecraftLauncher.exe (Sideloading)
- usysdiag.exe (Sideloading)

**Acknowledgement:** Andrew Oliveau
