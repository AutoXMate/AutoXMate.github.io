---
trust_level: community
id: windows-dllhijack-chrome-frame-helper
namespace: windows:dllhijack:chrome-frame-helper
name: chrome_frame_helper.dll
description: "chrome_frame_helper.dll — Sideloading hijacking (Google)"
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
  template: "chrome_frame_helper.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.hexacorn.com/blog/2016/03/10/beyond-good-ol-run-key-part-36/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/chrome-frame-helper.html"
---
examples:
  - description: "Place malicious chrome_frame_helper.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\Google\\Chrome\\Application\\chrome_frame_helper.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"chrome_frame_helper.exe\""

# chrome_frame_helper.dll

**Vendor:** Google

**Expected Location:** %LOCALAPPDATA%\Google\Chrome\Application

**Vulnerable Executables:**
- chrome_frame_helper.exe (Sideloading)

**Acknowledgement:** Adam
