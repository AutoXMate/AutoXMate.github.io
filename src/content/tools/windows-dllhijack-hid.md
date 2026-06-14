---
trust_level: community
id: windows-dllhijack-hid
namespace: windows:dllhijack:hid
name: hid.dll
description: "hid.dll — Sideloading, Search Order hijacking (Microsoft)"
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
  template: "hid.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://github.com/netero1010/ServiceMove-BOF"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/30fbf917d0a510b8dac3bacb0f4948f9d55bbfb0fa960b07f0af20ba4f18fc19/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/hid.html"
---
examples:
  - description: "Place malicious hid.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\hid.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\psr.exe\""

# hid.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\tabcal.exe (Sideloading)
- %SYSTEM32%\PerceptionSimulation\PerceptionSimulationService.exe (Search Order)
- %PROGRAMFILES%\Logitech\SetPointP\LDeviceDetectionHelper.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** v1stra

**Acknowledgement:** Still Hsu
