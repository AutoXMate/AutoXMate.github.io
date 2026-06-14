---
id: windows-kernel-amigendrv64
namespace: windows:kernel:amigendrv64
name: amigendrv64.sys
description: Elevate privileges
author: Nasreddine Bencherchali
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
  template: sc.exe create amigendrv64.sys binPath=C:\windows\temp\amigendrv64.sys
    type=kernel && sc.exe start amigendrv64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load amigendrv64.sys kernel driver
  commands:
  - sc.exe create amigendrv64.sys binPath=C:\windows\temp\amigendrv64.sys type=kernel
    && sc.exe start amigendrv64.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create amigendrv64.sys binPath=C:\\\\windows\\\\temp\\\\amigendrv64.sys type=kernel && sc.exe start amigendrv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver amigendrv64.sys"

# amigendrv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
