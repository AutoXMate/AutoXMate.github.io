---
trust_level: community
id: windows-dllhijack-iepdf32
namespace: windows:dllhijack:iepdf32
name: iepdf32.dll
description: "iepdf32.dll — Sideloading hijacking (HandySoftware)"
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
  template: "iepdf32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/b748e5dc64f5ece1b256705b7365a89b3be9284587da5f3abbde4be78864867e/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/030ca3bb54a276eea7cdf69d90d04b58a4fa500396e94340895f923d87dc169a/relations"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/iepdf32.html"
---
examples:
  - description: "Place malicious iepdf32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Handy Viewer\\iepdf32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Handy Viewer\\hv.exe\""

# iepdf32.dll

**Vendor:** HandySoftware

**Expected Location:** %PROGRAMFILES%\Handy Viewer

**Vulnerable Executables:**
- %PROGRAMFILES%\Handy Viewer\hv.exe (Sideloading)

**Acknowledgement:** Jai Minton
