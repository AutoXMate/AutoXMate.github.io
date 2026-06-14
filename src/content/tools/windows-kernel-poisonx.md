---
id: windows-kernel-poisonx
namespace: windows:kernel:poisonx
name: PoisonX.sys
description: A Microsoft-signed vulnerable driver used in BYOVD attacks to terminate
  protected processes, including EDR solutions such as CrowdStrike Falcon. The driver
  exposes an IOCTL that allows arbitrary process termination from user mode by passing
  a PID.
author: Bilal Retiat
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- defense-evasion
risk_level: high
trust_level: verified
execution:
  template: sc.exe create PoisonX.sys binPath=C:\windows\temp\PoisonX.sys type=kernel
    && sc.exe start PoisonX.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load PoisonX.sys kernel driver
  commands:
  - sc.exe create PoisonX.sys binPath=C:\windows\temp\PoisonX.sys type=kernel && sc.exe
    start PoisonX.sys
references:
- label: Reference
  url: https://medium.com/@jehadbudagga/reverse-engineering-a-0day-used-against-crowdstrike-edr-a5ea1fbe3fd4
- label: Reference
  url: https://github.com/j3h4ck/PoisonKiller/
features:
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create PoisonX.sys binPath=C:\\\\windows\\\\temp\\\\PoisonX.sys type=kernel && sc.exe start PoisonX.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PoisonX.sys"

# PoisonX.sys

A Microsoft-signed vulnerable driver used in BYOVD attacks to terminate protected processes, including EDR solutions such as CrowdStrike Falcon. The driver exposes an IOCTL that allows arbitrary process termination from user mode by passing a PID.

**Use Case:** Kill EDR / Privilege Escalation

**Required Privileges:** kernel

**MITRE ATT&CK:** T1562
