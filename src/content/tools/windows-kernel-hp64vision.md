---
id: windows-kernel-hp64vision
namespace: windows:kernel:hp64vision
name: hp64vision.sys
description: hp64vision.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create hp64vision binPath=C:\windows\temp\hp64vision.sys type=kernel
    && sc.exe start hp64vision
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load hp64vision.sys kernel driver
  commands:
  - sc.exe create hp64vision binPath=C:\windows\temp\hp64vision.sys type=kernel &&
    sc.exe start hp64vision
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
    command: "sc.exe create hp64vision binPath=C:\\\\windows\\\\temp\\\\hp64vision.sys type=kernel && sc.exe start hp64vision"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver hp64vision.sys"

# hp64vision.sys

hp64vision.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
