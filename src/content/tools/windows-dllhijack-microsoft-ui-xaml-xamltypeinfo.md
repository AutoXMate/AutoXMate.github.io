---
trust_level: community
id: windows-dllhijack-microsoft-ui-xaml-xamltypeinfo
namespace: windows:dllhijack:microsoft-ui-xaml-xamltypeinfo
name: microsoft.ui.xaml.xamltypeinfo.dll
description: "microsoft.ui.xaml.xamltypeinfo.dll — Phantom hijacking (Microsoft)"
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
  template: "microsoft.ui.xaml.xamltypeinfo.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://twitter.com/Octoberfest73/status/1631021071951437827/photo/1"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/microsoft-ui-xaml-xamltypeinfo.html"
---
examples:
  - description: "Place malicious microsoft.ui.xaml.xamltypeinfo.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\microsoft.ui.xaml.xamltypeinfo.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%LOCALAPPDATA%\\microsoft\\onedrive\\onedrive.exe\""

# microsoft.ui.xaml.xamltypeinfo.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %LOCALAPPDATA%\microsoft\onedrive\onedrive.exe (Phantom)
