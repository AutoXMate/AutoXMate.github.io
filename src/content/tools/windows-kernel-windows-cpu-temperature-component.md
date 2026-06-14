---
id: windows-kernel-windows-cpu-temperature-component
namespace: windows:kernel:windows-cpu-temperature-component
name: Windows_CPU_Temperature_Component.sys
description: Windows_CPU_Temperature_Component.sys is a vulnerable kernel driver from
  the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous
  kernel primitives to usermode.
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
  template: sc.exe create Windows_CPU_Temperature_Component binPath=C:\windows\temp\Windows_CPU_Temperature_Component.sys
    type=kernel && sc.exe start Windows_CPU_Temperature_Component
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Windows_CPU_Temperature_Component.sys kernel driver
  commands:
  - sc.exe create Windows_CPU_Temperature_Component binPath=C:\windows\temp\Windows_CPU_Temperature_Component.sys
    type=kernel && sc.exe start Windows_CPU_Temperature_Component
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
    command: "sc.exe create Windows_CPU_Temperature_Component binPath=C:\\\\windows\\\\temp\\\\Windows_CPU_Temperature_Component.sys type=kernel && sc.exe start Windows_CPU_Temperature_Component"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Windows_CPU_Temperature_Component.sys"

# Windows_CPU_Temperature_Component.sys

Windows_CPU_Temperature_Component.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
