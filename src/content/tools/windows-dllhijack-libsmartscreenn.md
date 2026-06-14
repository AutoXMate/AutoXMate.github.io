---
trust_level: community
id: windows-dllhijack-libsmartscreenn
namespace: windows:dllhijack:libsmartscreenn
name: libsmartscreenn.dll
description: "libsmartscreenn.dll — Sideloading hijacking (Microsoft)"
author: "Still Hsu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "libsmartscreenn.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/ead3b69fb1c4a8a7db7d89af55c75820ef76fce0d2fd341d5b2ea61b320f8821"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/ab89866a6c74eaee542e28b9401aa674ff2e7f73547cfa98eb685830d8b94887/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libsmartscreenn.html"
---
examples:
  - description: "Place malicious libsmartscreenn.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\WindowsApps\\Microsoft.DesktopAppInstaller_%VERSION%_x64__8wekyb3d8bbwe\\libsmartscreenn.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\WindowsApps\\Microsoft.DesktopAppInstaller_%VERSION%_x64__8wekyb3d8bbwe\\AppInstaller.exe\""

# libsmartscreenn.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\WindowsApps\Microsoft.DesktopAppInstaller_%VERSION%_x64__8wekyb3d8bbwe

**Vulnerable Executables:**
- %PROGRAMFILES%\WindowsApps\Microsoft.DesktopAppInstaller_%VERSION%_x64__8wekyb3d8bbwe\AppInstaller.exe (Sideloading)

**Acknowledgement:** Still Hsu
