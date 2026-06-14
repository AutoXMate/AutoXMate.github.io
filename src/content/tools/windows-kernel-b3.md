---
id: windows-kernel-b3
namespace: windows:kernel:b3
name: b3.sys
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
  template: sc.exe create b3.sys binPath=C:\windows\temp\b3.sys type=kernel && sc.exe
    start b3.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load b3.sys kernel driver
  commands:
  - sc.exe create b3.sys binPath=C:\windows\temp\b3.sys type=kernel && sc.exe start
    b3.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create b3.sys binPath=C:\\\\windows\\\\temp\\\\b3.sys type=kernel && sc.exe start b3.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver b3.sys"

# b3.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
