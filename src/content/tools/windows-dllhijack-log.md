---
trust_level: community
id: windows-dllhijack-log
namespace: windows:dllhijack:log
name: log.dll
description: "log.dll — Sideloading hijacking (BitDefender)"
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
  template: "log.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.secureworks.com/research/shadowpad-malware-analysis"
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/"
  - label: "Reference"
    url: "https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/log.html"
---
examples:
  - description: "Place malicious log.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Bitdefender Antivirus Free\\log.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Bitdefender Antivirus Free\\BDReinit.exe\""

# log.dll

**Vendor:** BitDefender

**Expected Location:** %PROGRAMFILES%\Bitdefender Antivirus Free

**Vulnerable Executables:**
- %PROGRAMFILES%\Bitdefender Antivirus Free\BDReinit.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender Agent\%VERSION%\BDReinit.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender Agent\%VERSION%\x64\BDReinit.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender\Bitdefender Security\BDReinit.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender\Bitdefender Security App\BDReinit.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender Antivirus Free\BDSubWiz.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender Agent\%VERSION%\BDSubWiz.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender Agent\%VERSION%\x64\BDSubWiz.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender\Bitdefender Security\BDSubWiz.exe (Sideloading)
- %PROGRAMFILES%\Bitdefender\Bitdefender Security App\BDSubWiz.exe (Sideloading)

**Acknowledgement:** Daniel Koifman

**Acknowledgement:** Wietze
