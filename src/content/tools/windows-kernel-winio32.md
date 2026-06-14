---
id: windows-kernel-winio32
namespace: windows:kernel:winio32
name: WinIO32.sys
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
  template: sc.exe create WinIO32.sys binPath=C:\windows\temp\WinIO32.sys type=kernel
    && sc.exe start WinIO32.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIO32.sys kernel driver
  commands:
  - sc.exe create WinIO32.sys binPath=C:\windows\temp\WinIO32.sys type=kernel && sc.exe
    start WinIO32.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIO32.sys binPath=C:\\\\windows\\\\temp\\\\WinIO32.sys type=kernel && sc.exe start WinIO32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIO32.sys"

# WinIO32.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
