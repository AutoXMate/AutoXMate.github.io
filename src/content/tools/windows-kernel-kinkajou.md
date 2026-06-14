---
id: windows-kernel-kinkajou
namespace: windows:kernel:kinkajou
name: Kinkajou.sys
description: Kinkajou.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create Kinkajou binPath=C:\windows\temp\Kinkajou.sys type=kernel
    && sc.exe start Kinkajou
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Kinkajou.sys kernel driver
  commands:
  - sc.exe create Kinkajou binPath=C:\windows\temp\Kinkajou.sys type=kernel && sc.exe
    start Kinkajou
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
    command: "sc.exe create Kinkajou binPath=C:\\\\windows\\\\temp\\\\Kinkajou.sys type=kernel && sc.exe start Kinkajou"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Kinkajou.sys"

# Kinkajou.sys

Kinkajou.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
