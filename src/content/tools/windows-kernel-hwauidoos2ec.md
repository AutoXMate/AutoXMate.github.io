---
id: windows-kernel-hwauidoos2ec
namespace: windows:kernel:hwauidoos2ec
name: HWAuidoOs2Ec.sys
description: HWAuidoOs2Ec.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create HWAuidoOs2Ec binPath=C:\windows\temp\HWAuidoOs2Ec.sys type=kernel
    && sc.exe start HWAuidoOs2Ec
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load HWAuidoOs2Ec.sys kernel driver
  commands:
  - sc.exe create HWAuidoOs2Ec binPath=C:\windows\temp\HWAuidoOs2Ec.sys type=kernel
    && sc.exe start HWAuidoOs2Ec
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
    command: "sc.exe create HWAuidoOs2Ec binPath=C:\\\\windows\\\\temp\\\\HWAuidoOs2Ec.sys type=kernel && sc.exe start HWAuidoOs2Ec"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver HWAuidoOs2Ec.sys"

# HWAuidoOs2Ec.sys

HWAuidoOs2Ec.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
