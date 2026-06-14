---
id: windows-kernel-realtime-driver
namespace: windows:kernel:realtime-driver
name: Realtime Driver.sys
description: Realtime Driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create Realtime Driver binPath=C:\windows\temp\Realtime Driver.sys
    type=kernel && sc.exe start Realtime Driver
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Realtime Driver.sys kernel driver
  commands:
  - sc.exe create Realtime Driver binPath=C:\windows\temp\Realtime Driver.sys type=kernel
    && sc.exe start Realtime Driver
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
    command: "sc.exe create Realtime Driver binPath=C:\\\\windows\\\\temp\\\\Realtime Driver.sys type=kernel && sc.exe start Realtime Driver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Realtime Driver.sys"

# Realtime Driver.sys

Realtime Driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
