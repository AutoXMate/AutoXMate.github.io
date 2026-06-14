---
id: windows-kernel-1
namespace: windows:kernel:1
name: 1.sys
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
  template: sc.exe create 1.sys binPath=C:\windows\temp\1.sys type=kernel && sc.exe
    start 1.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load 1.sys kernel driver
  commands:
  - sc.exe create 1.sys binPath=C:\windows\temp\1.sys type=kernel && sc.exe start
    1.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 1.sys binPath=C:\\\\windows\\\\temp\\\\1.sys type=kernel && sc.exe start 1.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 1.sys"

# 1.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
