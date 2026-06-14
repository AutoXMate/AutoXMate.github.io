---
id: windows-kernel-chinese-cheat-driver
namespace: windows:kernel:chinese-cheat-driver
name: chinese_cheat_driver.sys
description: chinese_cheat_driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create chinese_cheat_driver binPath=C:\windows\temp\chinese_cheat_driver.sys
    type=kernel && sc.exe start chinese_cheat_driver
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load chinese_cheat_driver.sys kernel driver
  commands:
  - sc.exe create chinese_cheat_driver binPath=C:\windows\temp\chinese_cheat_driver.sys
    type=kernel && sc.exe start chinese_cheat_driver
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
    command: "sc.exe create chinese_cheat_driver binPath=C:\\\\windows\\\\temp\\\\chinese_cheat_driver.sys type=kernel && sc.exe start chinese_cheat_driver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver chinese_cheat_driver.sys"

# chinese_cheat_driver.sys

chinese_cheat_driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
