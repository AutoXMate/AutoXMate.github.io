---
id: windows-kernel-gpcidrv64
namespace: windows:kernel:gpcidrv64
name: "gpcidrv64.sys"
description: "firmware erasing/modification"
author: "Takahiro Haruyama"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: "sc.exe create gpcidrv64.sys binPath=C:\\windows\\temp\\gpcidrv64.sys type=kernel && sc.exe start gpcidrv64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load gpcidrv64.sys kernel driver"
    commands:
      - "sc.exe create gpcidrv64.sys binPath=C:\\windows\\temp\\gpcidrv64.sys type=kernel && sc.exe start gpcidrv64.sys"
references:
  - label: "Reference"
    url: "https://github.com/ucsb-seclab/popkorn-artifact/tree/main/evaluation"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create gpcidrv64.sys binPath=C:\\\\windows\\\\temp\\\\gpcidrv64.sys type=kernel && sc.exe start gpcidrv64.sys"

# gpcidrv64.sys

**Use Case:** firmware erasing/modification

**Required Privileges:** kernel

**MITRE ATT&CK:** T1542