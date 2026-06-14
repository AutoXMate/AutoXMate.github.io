---
trust_level: community
id: windows-dllhijack-tedutil
namespace: windows:dllhijack:tedutil
name: tedutil.dll
description: "tedutil.dll — Sideloading hijacking (Microsoft)"
author: "Jai Minton - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "tedutil.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/eb014e37fdcaf42c93f606058896ccb47eed56be5e1701c7b9744bac0003a8e8/details"
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/win32/medfound/topoedit-modules"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tedutil.html"
---
examples:
  - description: "Place malicious tedutil.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft SDKs\\Windows\\%VERSION%\\Bin\\tedutil.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft SDKs\\Windows\\%VERSION%\\Bin\\TopoEdit.exe\""

# tedutil.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft SDKs\Windows\%VERSION%\Bin

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft SDKs\Windows\%VERSION%\Bin\TopoEdit.exe (Sideloading)

**Acknowledgement:** Jai Minton
