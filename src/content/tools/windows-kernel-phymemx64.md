---
id: windows-kernel-phymemx64
namespace: windows:kernel:phymemx64
name: Phymemx64.sys
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
  template: sc.exe create Phymemx64.sys binPath=C:\windows\temp\Phymemx64.sys type=kernel
    && sc.exe start Phymemx64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Phymemx64.sys kernel driver
  commands:
  - sc.exe create Phymemx64.sys binPath=C:\windows\temp\Phymemx64.sys type=kernel
    && sc.exe start Phymemx64.sys
references:
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Phymemx64.sys binPath=C:\\\\windows\\\\temp\\\\Phymemx64.sys type=kernel && sc.exe start Phymemx64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Phymemx64.sys"

# Phymemx64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
