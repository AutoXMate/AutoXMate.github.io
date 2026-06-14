---
id: windows-kernel-b
namespace: windows:kernel:b
name: b.sys
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
  template: sc.exe create b.sys binPath=C:\windows\temp\b.sys type=kernel && sc.exe
    start b.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load b.sys kernel driver
  commands:
  - sc.exe create b.sys binPath=C:\windows\temp\b.sys type=kernel && sc.exe start
    b.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create b.sys binPath=C:\\\\windows\\\\temp\\\\b.sys type=kernel && sc.exe start b.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver b.sys"

# b.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
