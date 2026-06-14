---
id: windows-kernel-smep-capcom
namespace: windows:kernel:smep-capcom
name: "smep_capcom.sys"
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
  template: "sc.exe create smep_capcom.sys binPath=C:\\windows\\temp\\smep_capcom.sys     type=kernel && sc.exe start smep_capcom.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load smep_capcom.sys kernel driver"
    commands:
      - "sc.exe create smep_capcom.sys binPath=C:\\windows\\temp\\smep_capcom.sys     type=kernel && sc.exe start smep_capcom.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create smep_capcom.sys binPath=C:\\\\windows\\\\temp\\\\smep_capcom.sys     type=kernel && sc.exe start smep_capcom.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver smep_capcom.sys"

# smep_capcom.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068