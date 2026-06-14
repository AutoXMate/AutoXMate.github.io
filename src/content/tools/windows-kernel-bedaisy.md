---
id: windows-kernel-bedaisy
namespace: windows:kernel:bedaisy
name: bedaisy.sys
description: BattlEye Anti-Cheat BEDAISY.SYS PPL privesc.
author: Wack0
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
  template: sc.exe create BEDaisy.sys binPath=C:\windows\temp\BEDaisy.sys type=kernel
    && sc.exe start BEDaisy.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load bedaisy.sys kernel driver
  commands:
  - sc.exe create BEDaisy.sys binPath=C:\windows\temp\BEDaisy.sys type=kernel && sc.exe
    start BEDaisy.sys
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/23
- label: Reference
  url: https://infosec.exchange/@Rairii/109310279380973806
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BEDaisy.sys binPath=C:\\\\windows\\\\temp\\\\BEDaisy.sys type=kernel && sc.exe start BEDaisy.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver bedaisy.sys"

# bedaisy.sys

BattlEye Anti-Cheat BEDAISY.SYS PPL privesc.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
