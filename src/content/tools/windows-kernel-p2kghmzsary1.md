---
id: windows-kernel-p2kghmzsary1
namespace: windows:kernel:p2kghmzsary1
name: p2KGhmzsARY1.sys
description: p2KGhmzsARY1.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create p2KGhmzsARY1 binPath=C:\windows\temp\p2KGhmzsARY1.sys type=kernel
    && sc.exe start p2KGhmzsARY1
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load p2KGhmzsARY1.sys kernel driver
  commands:
  - sc.exe create p2KGhmzsARY1 binPath=C:\windows\temp\p2KGhmzsARY1.sys type=kernel
    && sc.exe start p2KGhmzsARY1
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
    command: "sc.exe create p2KGhmzsARY1 binPath=C:\\\\windows\\\\temp\\\\p2KGhmzsARY1.sys type=kernel && sc.exe start p2KGhmzsARY1"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver p2KGhmzsARY1.sys"

# p2KGhmzsARY1.sys

p2KGhmzsARY1.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
