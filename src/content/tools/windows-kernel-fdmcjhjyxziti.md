---
id: windows-kernel-fdmcjhjyxziti
namespace: windows:kernel:fdmcjhjyxziti
name: FDMCJHJYXZITI.sys
description: FDMCJHJYXZITI.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create FDMCJHJYXZITI binPath=C:\windows\temp\FDMCJHJYXZITI.sys
    type=kernel && sc.exe start FDMCJHJYXZITI
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load FDMCJHJYXZITI.sys kernel driver
  commands:
  - sc.exe create FDMCJHJYXZITI binPath=C:\windows\temp\FDMCJHJYXZITI.sys type=kernel
    && sc.exe start FDMCJHJYXZITI
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- compression
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create FDMCJHJYXZITI binPath=C:\\\\windows\\\\temp\\\\FDMCJHJYXZITI.sys type=kernel && sc.exe start FDMCJHJYXZITI"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver FDMCJHJYXZITI.sys"

# FDMCJHJYXZITI.sys

FDMCJHJYXZITI.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
