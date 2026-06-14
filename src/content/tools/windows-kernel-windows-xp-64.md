---
id: windows-kernel-windows-xp-64
namespace: windows:kernel:windows-xp-64
name: windows-xp-64.sys
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
  template: sc.exe create windows-xp-64.sys binPath=C:\windows\temp\windows-xp-64.sys     type=kernel
    type=kernel && sc.exe start windows-xp-64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load windows-xp-64.sys kernel driver
  commands:
  - sc.exe create windows-xp-64.sys binPath=C:\windows\temp\windows-xp-64.sys     type=kernel
    type=kernel && sc.exe start windows-xp-64.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create windows-xp-64.sys binPath=C:\\\\windows\\\\temp\\\\windows-xp-64.sys     type=kernel type=kernel && sc.exe start windows-xp-64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver windows-xp-64.sys"

# windows-xp-64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
