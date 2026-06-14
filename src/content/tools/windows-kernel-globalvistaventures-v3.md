---
id: windows-kernel-globalvistaventures-v3
namespace: windows:kernel:globalvistaventures-v3
name: GlobalVistaVentures_v3.sys
description: GlobalVistaVentures_v3.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create GlobalVistaVentures_v3 binPath=C:\windows\temp\GlobalVistaVentures_v3.sys
    type=kernel && sc.exe start GlobalVistaVentures_v3
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load GlobalVistaVentures_v3.sys kernel driver
  commands:
  - sc.exe create GlobalVistaVentures_v3 binPath=C:\windows\temp\GlobalVistaVentures_v3.sys
    type=kernel && sc.exe start GlobalVistaVentures_v3
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
    command: "sc.exe create GlobalVistaVentures_v3 binPath=C:\\\\windows\\\\temp\\\\GlobalVistaVentures_v3.sys type=kernel && sc.exe start GlobalVistaVentures_v3"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GlobalVistaVentures_v3.sys"

# GlobalVistaVentures_v3.sys

GlobalVistaVentures_v3.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
