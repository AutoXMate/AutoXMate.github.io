---
trust_level: community
id: windows-dllhijack-libcef
namespace: windows:dllhijack:libcef
name: libcef.dll
description: "libcef.dll — Sideloading hijacking (Google)"
author: "Matt Anderson - HuntressLabs"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "libcef.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/24/c/cve-2024-21412--darkgate-operators-exploit-microsoft-windows-sma.html"
  - label: "Reference"
    url: "https://analyze.intezer.com/analyses/93e92d7a-9a46-4c1c-8ac0-87b4453beeb8"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/64d0fc47fd77eb300942602a912ea9403960acd4f2ed33a8e325594bf700d65f"
  - label: "Reference"
    url: "https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/libcef.html"
---
examples:
  - description: "Place malicious libcef.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\NVIDIA Corporation\\NVIDIA GeForce Experience\\libcef.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%Program Files\""

# libcef.dll

**Vendor:** Google

**Expected Location:** %PROGRAMFILES%\NVIDIA Corporation\NVIDIA GeForce Experience

**Vulnerable Executables:**
- %Program Files (x86)\NVIDIA Corporation\NVIDIA GeForce Experience\NVIDA Share.exe (Sideloading)

**Acknowledgement:** Matt Anderson
