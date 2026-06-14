---
id: windows-kernel-winiodrv
namespace: windows:kernel:winiodrv
name: WINIODrv.sys
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
  template: sc.exe create WINIODrv.sys binPath=C:\windows\temp\WINIODrv.sys type=kernel
    && sc.exe start WINIODrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WINIODrv.sys kernel driver
  commands:
  - sc.exe create WINIODrv.sys binPath=C:\windows\temp\WINIODrv.sys type=kernel &&
    sc.exe start WINIODrv.sys
references:
- label: Reference
  url: https://github.com/namazso/physmem_drivers
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WINIODrv.sys binPath=C:\\\\windows\\\\temp\\\\WINIODrv.sys type=kernel && sc.exe start WINIODrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WINIODrv.sys"

# WINIODrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
