---
trust_level: community
id: windows-dllhijack-endpointdlp
namespace: windows:dllhijack:endpointdlp
name: endpointdlp.dll
description: "endpointdlp.dll — Sideloading hijacking (Microsoft)"
author: "Jose Oregon"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "endpointdlp.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/28f0f4c19d290c74a2e2d20004e1eaccb062fb99f53254ba3810eeec29c191cc"
  - label: "Reference"
    url: "https://www.reddit.com/r/blueteamsec/comments/1sur3eh/observed_staged_endpoint_dlp_masquerade_dll/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/endpointdlp.html"
---
examples:
  - description: "Place malicious endpointdlp.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMDATA%\\Microsoft\\Windows Defender\\Platform\\%VERSION%\\endpointdlp.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMDATA%\\Microsoft\\Windows Defender\\Platform\\%VERSION%\\mpextms.exe\""

# endpointdlp.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMDATA%\Microsoft\Windows Defender\Platform\%VERSION%

**Vulnerable Executables:**
- %PROGRAMDATA%\Microsoft\Windows Defender\Platform\%VERSION%\mpextms.exe (Sideloading)

**Acknowledgement:** Jose Oregon
