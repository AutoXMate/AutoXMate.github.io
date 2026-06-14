---
trust_level: community
id: windows-dllhijack-vntfxf32
namespace: windows:dllhijack:vntfxf32
name: vntfxf32.dll
description: "vntfxf32.dll — Sideloading hijacking (VentaFax)"
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
  template: "vntfxf32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vntfxf32.html"
---
examples:
  - description: "Place malicious vntfxf32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Venta\\VentaFax & Voice\\vntfxf32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Venta\\VentaFax & Voice\\spoololk.exe\""

# vntfxf32.dll

**Vendor:** VentaFax

**Expected Location:** %PROGRAMFILES%\Venta\VentaFax & Voice

**Vulnerable Executables:**
- %PROGRAMFILES%\Venta\VentaFax & Voice\spoololk.exe (Sideloading)
