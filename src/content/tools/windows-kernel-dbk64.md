---
id: windows-kernel-dbk64
namespace: windows:kernel:dbk64
name: dbk64.sys
description: Elevate privileges
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
  template: sc.exe create dbk64.sys binPath=C:\windows\temp\dbk64.sys type=kernel
    && sc.exe start dbk64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dbk64.sys kernel driver
  commands:
  - sc.exe create dbk64.sys binPath=C:\windows\temp\dbk64.sys type=kernel && sc.exe
    start dbk64.sys
references:
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dbk64.sys binPath=C:\\\\windows\\\\temp\\\\dbk64.sys type=kernel && sc.exe start dbk64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dbk64.sys"

# dbk64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
