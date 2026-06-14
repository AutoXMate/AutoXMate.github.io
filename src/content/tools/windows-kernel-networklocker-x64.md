---
id: windows-kernel-networklocker-x64
namespace: windows:kernel:networklocker-x64
name: NetworkLocker_x64.sys
description: NetworkLocker_x64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create NetworkLocker_x64 binPath=C:\windows\temp\NetworkLocker_x64.sys
    type=kernel && sc.exe start NetworkLocker_x64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load NetworkLocker_x64.sys kernel driver
  commands:
  - sc.exe create NetworkLocker_x64 binPath=C:\windows\temp\NetworkLocker_x64.sys
    type=kernel && sc.exe start NetworkLocker_x64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- network-intensive
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NetworkLocker_x64 binPath=C:\\\\windows\\\\temp\\\\NetworkLocker_x64.sys type=kernel && sc.exe start NetworkLocker_x64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NetworkLocker_x64.sys"

# NetworkLocker_x64.sys

NetworkLocker_x64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
