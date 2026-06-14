---
trust_level: community
id: windows-dllhijack-sentinelagentcore
namespace: windows:dllhijack:sentinelagentcore
name: sentinelagentcore.dll
description: "sentinelagentcore.dll — Sideloading hijacking (SentinelOne)"
author: "Amelia Casley"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "sentinelagentcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/pe4Chscreeching/status/1955624714241810488"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/sentinelagentcore.html"
---
examples:
  - description: "Place malicious sentinelagentcore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\SentinelOne\\Sentinel Agent %VERSION%\\sentinelagentcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\SentinelOne\\Sentinel Agent %VERSION%\\SentinelBrowserNativeHost.exe\""

# sentinelagentcore.dll

**Vendor:** SentinelOne

**Expected Location:** %PROGRAMFILES%\SentinelOne\Sentinel Agent %VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\SentinelOne\Sentinel Agent %VERSION%\SentinelBrowserNativeHost.exe (Sideloading)
- %PROGRAMFILES%\SentinelOne\Sentinel Agent %VERSION%\SentinelAgentWorker.exe (Sideloading)

**Acknowledgement:** Amelia Casley

**Acknowledgement:** Tanner Filip
