---
trust_level: community
id: windows-dllhijack-roboform-x64
namespace: windows:dllhijack:roboform-x64
name: roboform-x64.dll
description: "roboform-x64.dll — Sideloading hijacking (Siber Systems)"
author: "Rick Gatenby"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "roboform-x64.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/25/b/updated-shadowpad-malware-leads-to-ransomware-deployment.html"
  - label: "Reference"
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_robform.yml"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/roboform-x64.html"
---
examples:
  - description: "Place malicious roboform-x64.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Siber Systems\\AI RoboForm\\%VERSION%\\roboform-x64.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Siber Systems\\AI RoboForm\\%VERSION%\\robotaskbaricon-x64.exe\""

# roboform-x64.dll

**Vendor:** Siber Systems

**Expected Location:** %PROGRAMFILES%\Siber Systems\AI RoboForm\%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Siber Systems\AI RoboForm\%VERSION%\robotaskbaricon-x64.exe (Sideloading)

**Acknowledgement:** Rick Gatenby
