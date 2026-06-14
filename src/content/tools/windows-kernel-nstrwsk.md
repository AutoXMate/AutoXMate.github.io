---
id: windows-kernel-nstrwsk
namespace: windows:kernel:nstrwsk
name: nstrwsk.sys
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
  template: sc.exe create nstrwsk.sys binPath=C:\windows\temp \n \n \n  strwsk.sys
    type=kernel && sc.exe start nstrwsk.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load nstrwsk.sys kernel driver
  commands:
  - sc.exe create nstrwsk.sys binPath=C:\windows\temp \n \n \n  strwsk.sys type=kernel
    && sc.exe start nstrwsk.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nstrwsk.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  strwsk.sys type=kernel && sc.exe start nstrwsk.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nstrwsk.sys"

# nstrwsk.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
