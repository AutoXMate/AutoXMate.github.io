---
id: windows-kernel-d
namespace: windows:kernel:d
name: d.sys
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
  template: sc.exe create d.sys binPath=C:\windows\temp\d.sys type=kernel && sc.exe
    start d.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load d.sys kernel driver
  commands:
  - sc.exe create d.sys binPath=C:\windows\temp\d.sys type=kernel && sc.exe start
    d.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create d.sys binPath=C:\\\\windows\\\\temp\\\\d.sys type=kernel && sc.exe start d.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver d.sys"

# d.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
