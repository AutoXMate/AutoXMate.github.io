---
id: windows-kernel-smep-namco
namespace: windows:kernel:smep-namco
name: "smep_namco.sys"
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
  template: "sc.exe create smep_namco.sys binPath=C:\\windows\\temp\\smep_namco.sys type=kernel && sc.exe start smep_namco.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load smep_namco.sys kernel driver"
    commands:
      - "sc.exe create smep_namco.sys binPath=C:\\windows\\temp\\smep_namco.sys type=kernel && sc.exe start smep_namco.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create smep_namco.sys binPath=C:\\\\windows\\\\temp\\\\smep_namco.sys type=kernel && sc.exe start smep_namco.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver smep_namco.sys"

# smep_namco.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068