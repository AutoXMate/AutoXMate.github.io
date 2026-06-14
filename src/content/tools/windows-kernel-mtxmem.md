---
id: windows-kernel-mtxmem
namespace: windows:kernel:mtxmem
name: mtxmem.sys
description: mtxmem.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
  repository. The driver exposes dangerous kernel primitives to usermode.
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
  template: sc.exe create mtxmem binPath=C:\windows\temp\mtxmem.sys type=kernel &&
    sc.exe start mtxmem
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load mtxmem.sys kernel driver
  commands:
  - sc.exe create mtxmem binPath=C:\windows\temp\mtxmem.sys type=kernel && sc.exe
    start mtxmem
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mtxmem binPath=C:\\\\windows\\\\temp\\\\mtxmem.sys type=kernel && sc.exe start mtxmem"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mtxmem.sys"

# mtxmem.sys

mtxmem.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
