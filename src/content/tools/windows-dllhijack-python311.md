---
trust_level: community
id: windows-dllhijack-python311
namespace: windows:dllhijack:python311
name: python311.dll
description: "python311.dll — Sideloading hijacking (Python)"
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
  template: "python311.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.securonix.com/blog/seolurker-attack-campaign-uses-seo-poisoning-fake-google-ads-to-install-malware/"
  - label: "Reference"
    url: "https://thedfirreport.com/2024/09/30/nitrogen-campaign-drops-sliver-and-ends-with-blackcat-ransomware/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/9514035fea8000a664799e369ae6d3af6abfe8e5cda23cdafbede83051692e63"
  - label: "Reference"
    url: "https://www.rapid7.com/blog/post/2024/05/13/ongoing-malvertising-campaign-leads-to-ransomware/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/python311.html"
---
examples:
  - description: "Place malicious python311.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Python311\\python311.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"pythonw.exe\""

# python311.dll

**Vendor:** Python

**Expected Location:** %PROGRAMFILES%\Python311

**Vulnerable Executables:**
- pythonw.exe (Sideloading)

**Acknowledgement:** Swachchhanda Shrawan Poudel
