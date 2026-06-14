---
id: windows-kernel-piddrv
namespace: windows:kernel:piddrv
name: piddrv.sys
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
trust_level: community
execution:
  template: sc.exe create piddrv.sys binPath=C:\windows\temp\piddrv.sys type=kernel
    && sc.exe start piddrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load piddrv.sys kernel driver
  commands:
  - sc.exe create piddrv.sys binPath=C:\windows\temp\piddrv.sys type=kernel && sc.exe
    start piddrv.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create piddrv.sys binPath=C:\\\\windows\\\\temp\\\\piddrv.sys type=kernel && sc.exe start piddrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver piddrv.sys"

# piddrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
