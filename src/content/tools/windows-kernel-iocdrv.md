---
id: windows-kernel-iocdrv
namespace: windows:kernel:iocdrv
name: "iOCdrv.sys"
description: "iOCdrv.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create iOCdrv binPath=C:\\windows\\temp\\iOCdrv.sys type=kernel && sc.exe start iOCdrv"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load iOCdrv.sys kernel driver"
    commands:
      - "sc.exe create iOCdrv binPath=C:\\windows\\temp\\iOCdrv.sys type=kernel && sc.exe start iOCdrv"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create iOCdrv binPath=C:\\\\windows\\\\temp\\\\iOCdrv.sys type=kernel && sc.exe start iOCdrv"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver iOCdrv.sys"

# iOCdrv.sys

iOCdrv.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068