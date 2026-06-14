---
trust_level: community
id: windows-dllhijack-epnsm
namespace: windows:dllhijack:epnsm
name: epnsm.dll
description: "epnsm.dll — Sideloading hijacking (seiko)"
author: "Jai Minton"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "epnsm.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d70cd4df89b101f34ea6b17bc07a88b096bae2220fb04e200443b09a2b681091/relations"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/8313f3970982cbd425a0c769c8a690fef456d31d321c7de1e588e572948afed9/details"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/epnsm.html"
---
examples:
  - description: "Place malicious epnsm.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Epson Software\\Document Capture Server\\epnsm.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Epson Software\\Document Capture Server\\EEventManager.exe\""

# epnsm.dll

**Vendor:** seiko

**Expected Location:** %PROGRAMFILES%\Epson Software\Document Capture Server

**Vulnerable Executables:**
- %PROGRAMFILES%\Epson Software\Document Capture Server\EEventManager.exe (Sideloading)

**Acknowledgement:** Jai Minton
