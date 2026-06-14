---
trust_level: community
id: windows-dllhijack-tts
namespace: windows:dllhijack:tts
name: tts.dll
description: tts.dll — Sideloading hijacking (LeppSoft)
author: Walter Gordillo
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: tts.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.virustotal.com/gui/file/9f45aadddaae7ad3076e0591fa4ccce302248c079dc07f5c9e3da788bdae0292/relations
- label: Reference
  url: https://www.virustotal.com/gui/file/af328ef3ae2c81a0ad5937cb186bb45d3190dbee390e180240e0a0218a1bce98
- label: HijackLibs
  url: https://hijacklibs.net/entries/tts.html
features:
- process-manip
---

examples:
  - description: "Place malicious tts.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Soundpad\\tts.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Soundpad\\Soundpad.exe\""

# tts.dll

**Vendor:** LeppSoft

**Expected Location:** %PROGRAMFILES%\Soundpad

**Vulnerable Executables:**
- %PROGRAMFILES%\Soundpad\Soundpad.exe (Sideloading)

**Acknowledgement:** Walter Gordillo
