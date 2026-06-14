---
trust_level: community
id: windows-dllhijack-basicnetutils
namespace: windows:dllhijack:basicnetutils
name: basicnetutils.dll
description: "basicnetutils.dll — Sideloading hijacking (Baidu)"
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
  template: "basicnetutils.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2023/05/03/doubled-dll-sideloading-dragon-breath/"
  - label: "Reference"
    url: "https://www.welivesecurity.com/2023/03/16/not-so-private-messaging-trojanized-whatsapp-telegram-cryptocurrency-wallets/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/basicnetutils.html"
---
examples:
  - description: "Place malicious basicnetutils.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Temp\\%VERSION%\\Application2\\basicnetutils.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\Temp\\%VERSION%\\Application2\\XLGameUpdate.exe\""

# basicnetutils.dll

**Vendor:** Baidu

**Expected Location:** %LOCALAPPDATA%\Temp\%VERSION%\Application2

**Vulnerable Executables:**
- %LOCALAPPDATA%\Temp\%VERSION%\Application2\XLGameUpdate.exe (Sideloading)
