---
id: windows-kernel-piddrv64
namespace: windows:kernel:piddrv64
name: piddrv64.sys
description: Elevate privileges
author: Michael Haag
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
  template: sc.exe create piddrv64.sys binPath=C:\windows\temp\piddrv64.sys type=kernel
    && sc.exe start piddrv64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load piddrv64.sys kernel driver
  commands:
  - sc.exe create piddrv64.sys binPath=C:\windows\temp\piddrv64.sys type=kernel &&
    sc.exe start piddrv64.sys
references:
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create piddrv64.sys binPath=C:\\\\windows\\\\temp\\\\piddrv64.sys type=kernel && sc.exe start piddrv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver piddrv64.sys"

# piddrv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
