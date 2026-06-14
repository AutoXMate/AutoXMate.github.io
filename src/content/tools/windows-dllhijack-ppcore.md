---
trust_level: community
id: windows-dllhijack-ppcore
namespace: windows:dllhijack:ppcore
name: ppcore.dll
description: "ppcore.dll — Sideloading hijacking (Microsoft)"
author: "Swachchhanda Shrawan Poudel"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "ppcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2025/apt29-phishing-campaign/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/d931078b63d94726d4be5dc1a00324275b53b935b77d3eed1712461f0c180164"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/ppcore.html"
---
examples:
  - description: "Place malicious ppcore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Microsoft Office\\OFFICE%VERSION%\\ppcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Microsoft Office\\OFFICE%VERSION%\\Powerpnt.exe\""

# ppcore.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Microsoft Office\OFFICE%VERSION%

**Vulnerable Executables:**
- %PROGRAMFILES%\Microsoft Office\OFFICE%VERSION%\Powerpnt.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office\Root\OFFICE%VERSION%\Powerpnt.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office %VERSION%\ClientX86\Root\Office%VERSION%\Powerpnt.exe (Sideloading)
- %PROGRAMFILES%\Microsoft Office %VERSION%\ClientX64\Root\Office%VERSION%\Powerpnt.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
