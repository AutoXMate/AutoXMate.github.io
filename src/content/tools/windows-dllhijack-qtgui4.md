---
trust_level: community
id: windows-dllhijack-qtgui4
namespace: windows:dllhijack:qtgui4
name: qtgui4.dll
description: "qtgui4.dll — Sideloading hijacking (Qt)"
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
  template: "qtgui4.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/dbdf5e11ec81ed1d941ec16fc7b94ab65f814ceb1e7fb524f2c64cbb422f7382/details"
  - label: "Reference"
    url: "https://forum.eset.com/topic/44610-im-afraid-i-did-something-stupid-and-im-usually-very-careful-i-keep-getting-an-address-has-been-blocked-message/page/2/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/qtgui4.html"
---
examples:
  - description: "Place malicious qtgui4.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Audacity\\qtgui4.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Audacity\\crashreporter.exe\""

# qtgui4.dll

**Vendor:** Qt

**Expected Location:** %PROGRAMFILES%\Audacity

**Vulnerable Executables:**
- %PROGRAMFILES%\Audacity\crashreporter.exe (Sideloading)
- %PROGRAMFILES%\AOMEI\AOMEI Backupper\%VERSION%\ShortcutTaskAgent.exe (Sideloading)

**Acknowledgement:** Jai Minton
