---
id: windows-kernel-gpu-z
namespace: windows:kernel:gpu-z
name: GPU-Z.sys
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
  template: sc.exe create GPU-Z.sys binPath=C:\windows\temp\GPU-Z.sys type=kernel
    && sc.exe start GPU-Z.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load GPU-Z.sys kernel driver
  commands:
  - sc.exe create GPU-Z.sys binPath=C:\windows\temp\GPU-Z.sys type=kernel && sc.exe
    start GPU-Z.sys
references:
- label: Reference
  url: https://github.com/myzxcg/RealBlindingEDR/
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create GPU-Z.sys binPath=C:\\\\windows\\\\temp\\\\GPU-Z.sys type=kernel && sc.exe start GPU-Z.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GPU-Z.sys"

# GPU-Z.sys

Utilized in RealBlindingEDR. 

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
