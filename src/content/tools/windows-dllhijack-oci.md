---
trust_level: community
id: windows-dllhijack-oci
namespace: windows:dllhijack:oci
name: oci.dll
description: "oci.dll — Phantom hijacking (Microsoft)"
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
  template: "oci.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/backdoor-at-the-end-of-the-icmp-tunnel/"
  - label: "Reference"
    url: "https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/oci.html"
---
examples:
  - description: "Place malicious oci.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\oci.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\msdtc.exe\""

# oci.dll

**Vendor:** Microsoft

**Vulnerable Executables:**
- %SYSTEM32%\msdtc.exe (Phantom)
