---
trust_level: community
id: windows-dllhijack-amindpdfcore
namespace: windows:dllhijack:amindpdfcore
name: amindpdfcore.dll
description: "amindpdfcore.dll — Sideloading hijacking (AmindPDF)"
author: "Still Hsu"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "amindpdfcore.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/78a60bea5693138c771386b8c22f0adfe6765a6313b80488bd1084bc9ed370bd"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/amindpdfcore.html"
---
examples:
  - description: "Place malicious amindpdfcore.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\GeekerPDF\\GeekerPDF\\amindpdfcore.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\GeekerPDF\\GeekerPDF\\GeekerPDF.exe\""

# amindpdfcore.dll

**Vendor:** AmindPDF

**Expected Location:** %PROGRAMFILES%\GeekerPDF\GeekerPDF

**Vulnerable Executables:**
- %PROGRAMFILES%\GeekerPDF\GeekerPDF\GeekerPDF.exe (Sideloading)

**Acknowledgement:** Still Hsu
