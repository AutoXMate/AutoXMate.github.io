---
id: windows-kernel-winio32a
namespace: windows:kernel:winio32a
name: WinIO32A.sys
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
  template: sc.exe create WinIO32A.sys binPath=C:\windows\temp\WinIO32A.sys type=kernel
    && sc.exe start WinIO32A.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIO32A.sys kernel driver
  commands:
  - sc.exe create WinIO32A.sys binPath=C:\windows\temp\WinIO32A.sys type=kernel &&
    sc.exe start WinIO32A.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIO32A.sys binPath=C:\\\\windows\\\\temp\\\\WinIO32A.sys type=kernel && sc.exe start WinIO32A.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIO32A.sys"

# WinIO32A.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
