---
id: windows-kernel-my
namespace: windows:kernel:my
name: My.sys
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
  template: sc.exe create My.sys binPath=C:\windows\temp\My.sys type=kernel && sc.exe
    start My.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load My.sys kernel driver
  commands:
  - sc.exe create My.sys binPath=C:\windows\temp\My.sys type=kernel && sc.exe start
    My.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create My.sys binPath=C:\\\\windows\\\\temp\\\\My.sys type=kernel && sc.exe start My.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver My.sys"

# My.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
