---
id: windows-kernel-winio64b
namespace: windows:kernel:winio64b
name: WinIo64B.sys
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
  template: sc.exe create WinIo64B.sys binPath=C:\windows\temp\WinIo64B.sys type=kernel
    && sc.exe start WinIo64B.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIo64B.sys kernel driver
  commands:
  - sc.exe create WinIo64B.sys binPath=C:\windows\temp\WinIo64B.sys type=kernel &&
    sc.exe start WinIo64B.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIo64B.sys binPath=C:\\\\windows\\\\temp\\\\WinIo64B.sys type=kernel && sc.exe start WinIo64B.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIo64B.sys"

# WinIo64B.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
