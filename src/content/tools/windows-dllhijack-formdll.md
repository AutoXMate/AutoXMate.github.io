---
trust_level: community
id: windows-dllhijack-formdll
namespace: windows:dllhijack:formdll
name: formdll.dll
description: "formdll.dll — Sideloading hijacking (Microsoft)"
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
  template: "formdll.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://any.run/report/d9c7f6d4ec08d961c20dac1b6422b3fbec5c6a8d9dc67d1f604835b36c5f224e/ae068531-92db-497d-b0cb-c0b1af5476f1"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/formdll.html"
---
examples:
  - description: "Place malicious formdll.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\Common Files\\Microsoft Shared\\NoteSync Forms\\formdll.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Common Files\\Microsoft Shared\\NoteSync Forms\\inkform.exe\""

# formdll.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\Common Files\Microsoft Shared\NoteSync Forms

**Vulnerable Executables:**
- %PROGRAMFILES%\Common Files\Microsoft Shared\NoteSync Forms\inkform.exe (Sideloading)
