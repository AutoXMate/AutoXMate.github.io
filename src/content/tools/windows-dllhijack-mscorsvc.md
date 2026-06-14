---
trust_level: community
id: windows-dllhijack-mscorsvc
namespace: windows:dllhijack:mscorsvc
name: mscorsvc.dll
description: "mscorsvc.dll — Phantom, Sideloading hijacking (Microsoft)"
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
  template: "mscorsvc.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "Reference"
    url: "https://www.securityjoes.com/post/hide-and-seek-in-windows-closet-unmasking-the-winsxs-hijacking-hideout"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/mscorsvc.html"
---
examples:
  - description: "Place malicious mscorsvc.dll in the search order location"
    command: "copy malicious.dll \"%WINDIR%\\Microsoft.NET\\Framework\\v%VERSION%\\mscorsvc.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%WINDIR%\\Microsoft.NET\\Framework\\v%VERSION%\\mscorsvw.exe\""

# mscorsvc.dll

**Vendor:** Microsoft

**Expected Location:** %WINDIR%\Microsoft.NET\Framework\v%VERSION%

**Vulnerable Executables:**
- %WINDIR%\Microsoft.NET\Framework\v%VERSION%\mscorsvw.exe (Sideloading)
- %WINDIR%\WinSxS\amd64_netfx4-ngentask_exe_%VERSION%\ngentask.exe (Phantom)

**Acknowledgement:** Michał Kucharski
