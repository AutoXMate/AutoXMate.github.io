---
id: windows-kernel-svioctrlx64
namespace: windows:kernel:svioctrlx64
name: SvIoCtrlx64.sys
description: SvIoCtrlx64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create SvIoCtrlx64 binPath=C:\windows\temp\SvIoCtrlx64.sys type=kernel
    && sc.exe start SvIoCtrlx64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load SvIoCtrlx64.sys kernel driver
  commands:
  - sc.exe create SvIoCtrlx64 binPath=C:\windows\temp\SvIoCtrlx64.sys type=kernel
    && sc.exe start SvIoCtrlx64
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
    command: "sc.exe create SvIoCtrlx64 binPath=C:\\\\windows\\\\temp\\\\SvIoCtrlx64.sys type=kernel && sc.exe start SvIoCtrlx64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SvIoCtrlx64.sys"

# SvIoCtrlx64.sys

SvIoCtrlx64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
