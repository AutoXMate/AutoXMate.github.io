---
trust_level: community
id: windows-dllhijack-rzlog4cpp-logger
namespace: windows:dllhijack:rzlog4cpp-logger
name: rzlog4cpp_logger.dll
description: "rzlog4cpp_logger.dll — Sideloading hijacking (Razer)"
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
  template: "rzlog4cpp_logger.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/china-nexus-espionage-southeast-asia"
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2022/11/03/family-tree-dll-sideloading-cases-may-be-related/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/rzlog4cpp-logger.html"
---
examples:
  - description: "Place malicious rzlog4cpp_logger.dll in the search order location"
    command: "copy malicious.dll \"%LOCALAPPDATA%\\razer\\InGameEngine\\cache\\RzFpsApplet\\rzlog4cpp_logger.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\razer\\InGameEngine\\cache\\RzFpsApplet\\RzCefRenderProcess.exe\""

# rzlog4cpp_logger.dll

**Vendor:** Razer

**Expected Location:** %LOCALAPPDATA%\razer\InGameEngine\cache\RzFpsApplet

**Vulnerable Executables:**
- %LOCALAPPDATA%\razer\InGameEngine\cache\RzFpsApplet\RzCefRenderProcess.exe (Sideloading)
