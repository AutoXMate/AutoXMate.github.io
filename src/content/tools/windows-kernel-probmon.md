---
id: windows-kernel-probmon
namespace: windows:kernel:probmon
name: probmon.sys
description: A vulnerable kernel driver that can be used to terminate arbitrary processes
author: Antonio Parata, Andrea Monzani
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- defense-evasion
risk_level: high
trust_level: verified
execution:
  template: sc.exe create probmon.sys binPath=C:\windows\temp\probmon.sys type=kernel
    && sc.exe start probmon.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load probmon.sys kernel driver
  commands:
  - sc.exe create probmon.sys binPath=C:\windows\temp\probmon.sys type=kernel && sc.exe
    start probmon.sys
references:
- label: Reference
  url: https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/
features:
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create probmon.sys binPath=C:\\\\windows\\\\temp\\\\probmon.sys type=kernel && sc.exe start probmon.sys"

# probmon.sys

A vulnerable kernel driver that can be used to terminate arbitrary processes

**Use Case:** EDR Kill

**Required Privileges:** Admin privileges

**MITRE ATT&CK:** T1562
