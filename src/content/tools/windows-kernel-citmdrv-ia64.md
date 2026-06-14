---
id: windows-kernel-citmdrv-ia64
namespace: windows:kernel:citmdrv-ia64
name: "CITMDRV_IA64.sys"
description: "Elevate privileges"
author: "Michael Haag"
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
  template: "sc.exe create CITMDRV_IA64.sys binPath=C:\\windows\\temp\\CITMDRV_IA64.sys     type=kernel && sc.exe start CITMDRV_IA64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CITMDRV_IA64.sys kernel driver"
    commands:
      - "sc.exe create CITMDRV_IA64.sys binPath=C:\\windows\\temp\\CITMDRV_IA64.sys     type=kernel && sc.exe start CITMDRV_IA64.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CITMDRV_IA64.sys binPath=C:\\\\windows\\\\temp\\\\CITMDRV_IA64.sys     type=kernel && sc.exe start CITMDRV_IA64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CITMDRV_IA64.sys"

# CITMDRV_IA64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068