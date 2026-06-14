---
id: windows-kernel-pmad
namespace: windows:kernel:pmad
name: PMAD.sys
description: PMAD.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create PMAD binPath=C:\windows\temp\PMAD.sys type=kernel && sc.exe
    start PMAD
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load PMAD.sys kernel driver
  commands:
  - sc.exe create PMAD binPath=C:\windows\temp\PMAD.sys type=kernel && sc.exe start
    PMAD
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
    command: "sc.exe create PMAD binPath=C:\\\\windows\\\\temp\\\\PMAD.sys type=kernel && sc.exe start PMAD"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PMAD.sys"

# PMAD.sys

PMAD.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
