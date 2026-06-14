---
trust_level: community
id: windows-dllhijack-shellchromeapi
namespace: windows:dllhijack:shellchromeapi
name: shellchromeapi.dll
description: "shellchromeapi.dll — Phantom hijacking (Microsoft)"
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
  template: "shellchromeapi.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://dennisbabkin.com/blog/?t=pwning-windows-updates-dll-hijacking-through-orphaned-dll"
  - label: "Reference"
    url: "https://twitter.com/0gtweet/status/1564131230941122561"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/shellchromeapi.html"
---
examples:
  - description: "Place malicious shellchromeapi.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\shellchromeapi.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\DeviceEnroller.exe\""

# shellchromeapi.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\DeviceEnroller.exe (Phantom)

**Acknowledgement:** Grzegorz Tworek
