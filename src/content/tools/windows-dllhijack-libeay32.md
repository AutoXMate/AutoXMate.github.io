---
trust_level: community
id: windows-dllhijack-libeay32
namespace: windows:dllhijack:libeay32
name: libeay32.dll
description: "libeay32.dll — Sideloading hijacking (PSPad)"
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
  template: "libeay32.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://asec.ahnlab.com/en/58319/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/cf801023465679ec34084bdb1adb9f54b2fc3130925a4b8fdc10b11639b4a7cd"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/7add49ed95d6a9e90988dcbfc54cdb727e0c705e3d79879717849798354e3e25"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/a13c09f41979df8717a9d39e15e6ce960c1c4ba6af456a563fa3ff1b8b4d388c"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libeay32.html"
---
examples:
  - description: "Place malicious libeay32.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\PSPad editor\\libeay32.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\PSPad editor\\PSPad.exe\""

# libeay32.dll

**Vendor:** PSPad

**Expected Location:** %PROGRAMFILES%\PSPad editor

**Vulnerable Executables:**
- %PROGRAMFILES%\PSPad editor\PSPad.exe (Sideloading)

**Acknowledgement:** Jai Minton
