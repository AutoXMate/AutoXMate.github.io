---
id: windows-kernel-citmdrv-amd64
namespace: windows:kernel:citmdrv-amd64
name: CITMDRV_AMD64.sys
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
  template: sc.exe create CITMDRV_AMD64.sys binPath=C:\windows\temp\CITMDRV_AMD64.sys     type=kernel
    && sc.exe start CITMDRV_AMD64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load CITMDRV_AMD64.sys kernel driver
  commands:
  - sc.exe create CITMDRV_AMD64.sys binPath=C:\windows\temp\CITMDRV_AMD64.sys     type=kernel
    && sc.exe start CITMDRV_AMD64.sys
references:
- label: Reference
  url: https://github.com/namazso/physmem_drivers
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CITMDRV_AMD64.sys binPath=C:\\\\windows\\\\temp\\\\CITMDRV_AMD64.sys     type=kernel && sc.exe start CITMDRV_AMD64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CITMDRV_AMD64.sys"

# CITMDRV_AMD64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
