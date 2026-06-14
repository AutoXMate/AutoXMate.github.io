---
trust_level: community
id: windows-dllhijack-tmtap
namespace: windows:dllhijack:tmtap
name: tmtap.dll
description: "tmtap.dll — Phantom hijacking (Trend Micro)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
  - security.privilegeescalation.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
  - privilege-escalation
execution:
  template: "tmtap.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://medium.com/@infiniti_css/trend-micro-password-manager-dll-hijack-fa839acaad59"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/tmtap.html"
---
examples:
  - description: "Place malicious tmtap.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\tmtap.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\trend micro\\passwordmanager\\pwmsvc.exe\""

# tmtap.dll

**Vendor:** Trend Micro

**Vulnerable Executables:**
- %PROGRAMFILES%\trend micro\passwordmanager\pwmsvc.exe (Phantom) [PrivEsc]
