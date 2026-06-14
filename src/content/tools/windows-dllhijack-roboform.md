---
trust_level: community
id: windows-dllhijack-roboform
namespace: windows:dllhijack:roboform
name: roboform.dll
description: roboform.dll — Sideloading hijacking (Siber Systems)
author: Rick Gatenby
version: 1.0.0
capabilities:
- security.defenseevasion.dll-hijack
platforms:
- windows
techniques:
- defense-evasion
- persistence
execution:
  template: roboform.dll
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Reference
  url: https://www.trendmicro.com/en_us/research/25/b/updated-shadowpad-malware-leads-to-ransomware-deployment.html
- label: Reference
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_robform.yml
- label: HijackLibs
  url: https://hijacklibs.net/entries/roboform.html
features:
- file-system
---

examples:
  - description: "Place malicious roboform.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Siber Systems\\AI RoboForm\\roboform.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Siber Systems\\AI RoboForm\\RoboTaskBarIcon.exe\""

# roboform.dll

**Vendor:** Siber Systems

**Expected Location:** %PROGRAMFILES%\Siber Systems\AI RoboForm

**Vulnerable Executables:**
- %PROGRAMFILES%\Siber Systems\AI RoboForm\RoboTaskBarIcon.exe (Sideloading)

**Acknowledgement:** Rick Gatenby
