---
id: windows-kernel-winio32b
namespace: windows:kernel:winio32b
name: WinIO32B.sys
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
  template: sc.exe create WinIO32B.sys binPath=C:\windows\temp\WinIO32B.sys type=kernel
    && sc.exe start WinIO32B.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIO32B.sys kernel driver
  commands:
  - sc.exe create WinIO32B.sys binPath=C:\windows\temp\WinIO32B.sys type=kernel &&
    sc.exe start WinIO32B.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIO32B.sys binPath=C:\\\\windows\\\\temp\\\\WinIO32B.sys type=kernel && sc.exe start WinIO32B.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIO32B.sys"

# WinIO32B.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
