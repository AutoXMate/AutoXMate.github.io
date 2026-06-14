---
id: windows-kernel-wnbios
namespace: windows:kernel:wnbios
name: wnbios.sys
description: 'Utilized in RealBlindingEDR. '
author: goosvorbook
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create wnbios.sys binPath=C:\windows\temp\wnbios.sys type=kernel
    && sc.exe start wnbios.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load wnbios.sys kernel driver
  commands:
  - sc.exe create wnbios.sys binPath=C:\windows\temp\wnbios.sys type=kernel && sc.exe
    start wnbios.sys
references:
- label: Reference
  url: https://github.com/myzxcg/RealBlindingEDR/
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wnbios.sys binPath=C:\\\\windows\\\\temp\\\\wnbios.sys type=kernel && sc.exe start wnbios.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wnbios.sys"

# wnbios.sys

Utilized in RealBlindingEDR. 

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
