---
id: windows-kernel-daxin-blank2
namespace: windows:kernel:daxin-blank2
name: "daxin_blank2.sys"
description: "Driver used in the Daxin malware campaign."
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create daxin_blank2.sys binPath=C:\\windows\\temp\\daxin_blank2.sys     type=kernel && sc.exe start daxin_blank2.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load daxin_blank2.sys kernel driver"
    commands:
      - "sc.exe create daxin_blank2.sys binPath=C:\\windows\\temp\\daxin_blank2.sys     type=kernel && sc.exe start daxin_blank2.sys"
references:
  - label: "Reference"
    url: "https://gist.github.com/MHaggis/9ab3bb795a6018d70fb11fa7c31f8f48"
  - label: "Reference"
    url: "https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/daxin-backdoor-espionage"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create daxin_blank2.sys binPath=C:\\\\windows\\\\temp\\\\daxin_blank2.sys     type=kernel && sc.exe start daxin_blank2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver daxin_blank2.sys"

# daxin_blank2.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068