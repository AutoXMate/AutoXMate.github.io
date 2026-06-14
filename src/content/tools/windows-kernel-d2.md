---
id: windows-kernel-d2
namespace: windows:kernel:d2
name: d2.sys
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
  template: sc.exe create d2.sys binPath=C:\windows\temp\d2.sys type=kernel && sc.exe
    start d2.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load d2.sys kernel driver
  commands:
  - sc.exe create d2.sys binPath=C:\windows\temp\d2.sys type=kernel && sc.exe start
    d2.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create d2.sys binPath=C:\\\\windows\\\\temp\\\\d2.sys type=kernel && sc.exe start d2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver d2.sys"

# d2.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
